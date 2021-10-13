import argparse
import json
from pathlib import Path
import os

def save_lisible(path, suffix="_lisible", save_to=Path.cwd()):
    if isinstance(path, str):
        path = Path(path)
    if path.is_file():
        with open(path, "r") as f:
            D = json.load(f)
        stem = path.stem if isinstance(path, Path) else os.path.splitext(os.path.basename(path))[0]
        with open(save_to / f"{stem}{suffix}.json", "w") as f:
            json.dump(D, f, ensure_ascii=False, indent=2)
    elif path.is_dir():
        save_to = Path(f"{path.name}_lisible")
        save_to.mkdir(parents=True, exist_ok=True)
        for p in path.iterdir():
            if p.suffix == ".json":
                save_lisible(p, suffix="", save_to=save_to)
    else:
        print("Nothing happens. The input path should be a JSON file or a folder of JSON files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path_json",
        help="path to a JSON file",
    )
    args = parser.parse_args()
    save_lisible(args.path_json)
