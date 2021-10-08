import json
from lisible import save_lisible


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

