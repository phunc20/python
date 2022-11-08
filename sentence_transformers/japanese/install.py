import argparse
from itertools import combinations

import torch
from sentence_transformers import (
    SentenceTransformer,
    util,
)
from transformers import BertJapaneseTokenizer, BertModel


# It seems that we cannot SentenceTransformer("sonoisa/sentence-bert-base-ja-mean-tokens")
# be it v1 or v2. Instead, we follow sonoisa's instructions
class SentenceBertJapanese:
    def __init__(self, model_name_or_path, device=None):
        self.tokenizer = BertJapaneseTokenizer.from_pretrained(model_name_or_path)
        self.model = BertModel.from_pretrained(model_name_or_path)
        self.model.eval()

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device)
        self.model.to(device)

    def _mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0] # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    @torch.no_grad()
    def encode(self, sentences, batch_size=8):
        all_embeddings = []
        iterator = range(0, len(sentences), batch_size)
        for batch_idx in iterator:
            batch = sentences[batch_idx:batch_idx + batch_size]

            encoded_input = self.tokenizer.batch_encode_plus(batch, padding="longest", 
                                           truncation=True, return_tensors="pt").to(self.device)
            model_output = self.model(**encoded_input)
            sentence_embeddings = self._mean_pooling(model_output, encoded_input["attention_mask"]).to('cpu')

            all_embeddings.extend(sentence_embeddings)

        # return torch.stack(all_embeddings).numpy()
        return torch.stack(all_embeddings)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PyTorch Example')
    parser.add_argument('--cuda', action='store_true',
                        help='Enable CUDA')
    args = parser.parse_args()
    args.device = None
    if args.cuda and torch.cuda.is_available():
        args.device = torch.device('cuda')
    else:
        args.device = torch.device('cpu')
    
    print("Install sonoisa's and colorfulscoop's models:")
    SentenceBertJapanese("sonoisa/sentence-bert-base-ja-mean-tokens", args.device)
    SentenceBertJapanese("sonoisa/sentence-bert-base-ja-mean-tokens-v2", args.device)
    SentenceTransformer("colorfulscoop/sbert-base-ja", device=args.device)
    
    sentences = [
        "暴走したAI",
        "暴走した人工知能",
        #"暴走的人工智慧",    # Taiwanese
        "使い方",
        "人間の知的能力",
    ]


    print("Test sonoisa's v1:")
    MODEL_NAME = "sonoisa/sentence-bert-base-ja-mean-tokens"
    model = SentenceBertJapanese(MODEL_NAME, args.device)
    embeddings = model.encode(sentences, batch_size=8)
    for ind1, ind2 in combinations(range(len(sentences)), 2):
        emb1 = embeddings[ind1]
        emb2 = embeddings[ind2]
        sent1 = sentences[ind1]
        sent2 = sentences[ind2]
        print(f"{sent1 = }")
        print(f"{sent2 = }")
        print(f"{util.cos_sim(emb1, emb2) = }")
        print()


    print("Test sonoisa's v2:")
    MODEL_NAME = "sonoisa/sentence-bert-base-ja-mean-tokens-v2"
    model = SentenceBertJapanese(MODEL_NAME, args.device)
    embeddings = model.encode(sentences, batch_size=8)
    
    for ind1, ind2 in combinations(range(len(sentences)), 2):
        emb1 = embeddings[ind1]
        emb2 = embeddings[ind2]
        sent1 = sentences[ind1]
        sent2 = sentences[ind2]
        print(f"{sent1 = }")
        print(f"{sent2 = }")
        print(f"{util.cos_sim(emb1, emb2) = }")
        print()



    print("Test colorfulscoop's:")
    model = SentenceTransformer("colorfulscoop/sbert-base-ja", device=args.device)
    embeddings = model.encode(sentences, batch_size=8)
    for ind1, ind2 in combinations(range(len(sentences)), 2):
        emb1 = embeddings[ind1]
        emb2 = embeddings[ind2]
        sent1 = sentences[ind1]
        sent2 = sentences[ind2]
        print(f"{sent1 = }")
        print(f"{sent2 = }")
        print(f"{util.cos_sim(emb1, emb2) = }")
        print()
