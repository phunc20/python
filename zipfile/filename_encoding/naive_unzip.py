from pathlib import Path
from zipfile import ZipFile
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "zip",
        help="path of the zip file to be unzipped",
    )
    parser.add_argument(
        "-d",
        "--dir",
        default=".",
        type=str,
        help="path to the dir where files be extracted",
    )
    args = parser.parse_args()

    #print(args)
    save_dir = Path(args.dir)
    save_dir.mkdir(exist_ok=True)

    with ZipFile(args.zip) as io:
        io.extractall(save_dir)


if __name__ == "__main__":
    main()
