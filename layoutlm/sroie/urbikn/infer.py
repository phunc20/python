import argparse
import os
import glob
import json 
import random
from pathlib import Path
#from difflib import SequenceMatcher
import cv2
import pandas as pd
import numpy as np
from PIL import Image, ImageOps
import pytesseract
from tqdm import tqdm
#from IPython.display import display
#import matplotlib
#from matplotlib import pyplot, patches

import torch
from torch.nn import CrossEntropyLoss

from transformers import (
    WEIGHTS_NAME,
    AdamW,
    BertConfig,
    BertForTokenClassification,
    BertTokenizer,
    get_linear_schedule_with_warmup,
)
from layoutlm import (
    FunsdDataset,
    LayoutlmConfig,
    LayoutlmForTokenClassification
)
from layoutlm.data.funsd import (
    read_examples_from_file,
    convert_examples_to_features,
)

def normalize(points: list, width: int, height: int) -> list:
    x0, y0, x2, y2 = [int(p) for p in points]
    x0 = int(1000 * (x0 / width))
    x2 = int(1000 * (x2 / width))
    y0 = int(1000 * (y0 / height))
    y2 = int(1000 * (y2 / height))

    return [x0, y0, x2, y2]

def write_dataset(filename: str, image: Image.Image, df: pd.DataFrame, output_dir: Path, name: str):
    print(f"writing {name}ing dataset:")
    with open(output_dir / f"{name}.txt", "w+", encoding="utf8") as file, \
         open(output_dir / f"{name}_box.txt", "w+", encoding="utf8") as file_bbox, \
         open(output_dir / f"{name}_image.txt", "w+", encoding="utf8") as file_image:

        width, height = image.size
        #filename = image.filename
        for index, row in df.iterrows():
            bbox = [int(p) for p in row[["left", "top", "right", "bottom"]]]
            normalized_bbox = normalize(bbox, width, height)

            file.write("{}\t{}\n".format(row['text'], "O"))  # we don't actually have labels so put all O's
            file_bbox.write("{}\t{} {} {} {}\n".format(row['text'], *normalized_bbox))
            file_image.write("{}\t{} {} {} {}\t{} {}\t{}\n".format(row['text'], *bbox, width, height, filename))

        # write a second newline to separate dataset from others
        file.write("\n")
        file_bbox.write("\n")
        file_image.write("\n")

def get_labels(path):
    with open(path, "r") as f:
        labels = f.read().splitlines()
    if "o" not in labels:
        labels = ["o"] + labels
    return labels

def infer_one_instance():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path_image",
        help="path of the receipt image in question",
    )
    parser.add_argument(
        "--ocr_engine",
        default="tesseract",
        type=str,
        help="type of ocr engine: tesseract/clova",
    )
    parser.add_argument(
        "--lang",
        default="jpn",
        type=str,
        help="language of the receipt: eng/jpn/jpn_vert",
    )
    args = parser.parse_args()

    path_image = Path(args.path_image)
    if not path_image.exists():
        print(f"error: inexistent --path_image {path_image}")
        exit()
    if args.ocr_engine not in ("tesseract", "clova"):
        print(f"error: invalid --ocr_engine {args.ocr_engine}")
        exit()
    if args.lang not in ("eng", "jpn", "jpn_vert"):
        print(f"error: invalid --lang {args.lang}")
        exit()

    # Load the image
    image = Image.open(path_image)
    #print(f"image.filename = {image.filename}")
    exif = image._getexif()
    orientation_key = 274
    if exif and exif.get(orientation_key):
        image = ImageOps.exif_transpose(image)
    #print(f"image.filename = {image.filename}")

    # OCr
    if args.ocr_engine == "tesseract":
        df = pytesseract.image_to_data(image, lang=args.lang, output_type="data.frame")
        df = df.dropna()
        df = df.assign(
            bottom = lambda x: x.top + x.height,
            right = lambda x: x.left + x.width,
        )
        print(df.head())
    else:  # clova
        stem = path_image.stem
        path_json = Path(f"lineocr_response_lisible/{stem}.json")
        with open(path_json, "r") as f:
            d = json.load(f)
        fields = d["images"][0]["fields"]
        d = {
            "left": [],
            "top": [],
            "right": [],
            "bottom": [],
            "text": [],
        }
        for f in fields:
            vertices = f["boundingPoly"]["vertices"]
            d["left"].append(int(vertices[0]["x"]))
            d["top"].append(int(vertices[0]["y"]))
            d["right"].append(int(vertices[2]["x"]))
            d["bottom"].append(int(vertices[2]["y"]))
            d["text"].append(f["inferText"])
        df = pd.DataFrame(data=d)
        #print(df.head())
        print(df)

    config_class, model_class, tokenizer_class = LayoutlmConfig, LayoutlmForTokenClassification, BertTokenizer
    do_lower_case = True
    pwd = Path.cwd()
    output_dir = Path.home() / "git-repos/github/microsoft/unilm/layoutlm/deprecated/examples/seq_labeling/output"
    model_name_or_path = Path("layoutlm-base-uncased")
    tokenizer = tokenizer_class.from_pretrained(
        str(model_name_or_path),
        do_lower_case=do_lower_case,
    )
    model = model_class.from_pretrained(str(output_dir))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    pad_token_label_id = CrossEntropyLoss().ignore_index

    write_dataset(path_image.name, image, df, Path("dataset"), "infer")
    labels = get_labels(Path("dataset/labels.txt"))
    data_dir = Path("dataset")
    mode = "infer"
    examples = read_examples_from_file(data_dir, mode)

    max_seq_length = 512
    features = convert_examples_to_features(
        examples,
        labels,
        max_seq_length,
        tokenizer,
        cls_token_at_end=False,
        cls_token=tokenizer.cls_token,
        cls_token_segment_id=0,
        sep_token=tokenizer.sep_token,
        sep_token_extra=False,
        pad_on_left=False,
        pad_token=tokenizer.convert_tokens_to_ids([tokenizer.pad_token])[0],
        pad_token_segment_id=0,
        pad_token_label_id=pad_token_label_id,
    )
    
    all_input_ids = torch.tensor(
        [f.input_ids for f in features], dtype=torch.long
    )
    all_input_mask = torch.tensor(
        [f.input_mask for f in features], dtype=torch.long
    )
    all_segment_ids = torch.tensor(
        [f.segment_ids for f in features], dtype=torch.long
    )
    all_label_ids = torch.tensor(
        [f.label_ids for f in features], dtype=torch.long
    )
    all_bboxes = torch.tensor([f.boxes for f in features], dtype=torch.long)
    batch = (
        all_input_ids,
        all_input_mask,
        all_segment_ids,
        all_label_ids,
        all_bboxes,
    )
    with torch.no_grad():
        inputs = {
            "input_ids": batch[0].to(device),
            "attention_mask": batch[1].to(device),
            "labels": batch[3].to(device),
        }
        inputs["bbox"] = batch[4].to(device)
        inputs["token_type_ids"] = batch[2].to(device)
        outputs = model(**inputs)
    tmp_eval_loss, logits = outputs[:2]
    preds = logits.detach().cpu().numpy()
    out_label_ids = inputs["labels"].detach().cpu().numpy()
    preds = np.argmax(preds, axis=2)
    label_map = {i: label for i, label in enumerate(labels)}
    out_label_list = [[] for _ in range(out_label_ids.shape[0])]
    preds_list = [[] for _ in range(out_label_ids.shape[0])]
                                                            
    for i in range(out_label_ids.shape[0]):
        for j in range(out_label_ids.shape[1]):
            if out_label_ids[i, j] != pad_token_label_id:
                out_label_list[i].append(label_map[out_label_ids[i][j]])
                preds_list[i].append(label_map[preds[i][j]])
    df["tag"] = preds_list[0]
    #print([" ".join(df["text"][df["tag"] == tag]) for tag in labels if tag != "O"])
    pred = {
        tag: " ".join(df["text"][df["tag"] == tag]) for tag in labels if tag != "O"}
    print(pred)


if __name__ == "__main__":
    infer_one_instance()
