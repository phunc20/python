import argparse
from pathlib import Path

import fitz


def get_lines(self, *, fixed_width=True, sort=False):
    blocks = self.get_text("blocks", sort=sort)
    lines = []
    for block in blocks:
        x0,y0,x2,y2 = block[:4]
        w, h = x2-x0, y2-y0
        texts = block[4].strip()
        if "\n" in texts:
            splits = texts.split("\n")
            n_splits = len(splits)
            max_chars = max(len(split) for split in splits)
            dh = h / n_splits
            for i, split in enumerate(splits[:-1]):
                xi0 = x0
                yi0 = y0 + i*dh

                if fixed_width:
                   xi2 = x2
                else:
                    dw = w * (len(split)/max_chars)
                    xi2 = x0 + dw

                yi2 = y0 + (i+1)*dh
                lines.append((xi0,yi0,xi2,yi2,split))
            # Last split
            i += 1
            split = splits[i]
            xi0 = x0
            yi0 = y0 + i*dh
            dw = w * (len(split)/max_chars)
            xi2 = x0 + dw
            lines.append((xi0,yi0,xi2,yi2,split))
        else:
            lines.append((x0,y0,x2,y2,texts))
    return lines


# Monkey patching
fitz.fitz.Page.get_lines = get_lines


def ocr_like_response(pdf_path="single_page.pdf", *, page_idx=0, output_type="blocks", fixed_width=False, sort=False):
    pdf_path = Path(pdf_path)
    if not pdf_path.is_file():
        raise FileNotFoundError(
            f"{pdf_path = } "
            "is either an invalid path or not a PDF file"
        )
    doc = fitz.open(pdf_path)
    page = doc[page_idx]
    if output_type == "blocks":
        return page.get_text("blocks", sort=sort)
    elif output_type == "lines":
        return page.get_lines(
            fixed_width=fixed_width,
            sort=sort,
        )
    else:
        raise ValueError(
            f"User specified {output_type = }. "
            "But only accepts \"blocks\" or \"lines\""
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--pdf",
        #nargs="?",
        #const="single_page.pdf",
        default="single_page.pdf",
        help="path to some PDF file",
    )
    args = parser.parse_args()
    response = ocr_like_response(args.pdf, output_type="lines", sort=True)
    print(f"{response = }")
