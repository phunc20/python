import argparse
import json
from pathlib import Path
import os

def save_lisible(filename):
    with open(filename, "r") as f:
        D = json.load(f)
    stem = filename.stem if isinstance(filename, Path) else os.path.splitext(os.path.basename(filename))[0]
    with open(f"{stem}_lisible.json", "w") as f:
        json.dump(D, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path_json",
        help="path to a JSON file",
    )
    args = parser.parse_args()
    save_lisible(args.path_json)
