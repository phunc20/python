import json
from pathlib import Path

def save_lisible(filename):
    with open(filename, "r") as f:
        D = json.load(f)
    stem = filename.stem if isinstance(filename, Path) else filename.split(".")[0]
    with open(f"{stem}_lisible.json", "w") as f:
        json.dump(D, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    D = {"身高": 175, "體重": 85}
    with open(f"body.json", "w") as f:
        json.dump(D, f)
    print(f"cat body.json")
    with open(f"body.json", "r") as f:
        print(f.read())
    save_lisible("body.json")
    print(f"cat body_lisible.json")
    with open(f"body_lisible.json", "r") as f:
        print(f.read())

