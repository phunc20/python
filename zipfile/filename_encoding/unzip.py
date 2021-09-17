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
        for filename in io.namelist():
            utf8_filename = filename.encode("cp437").decode("utf-8")
            #print(f"utf8_filename = {utf8_filename }")
            #help(io.extract)
            io.extract(filename, save_dir)
            (save_dir/filename).rename(save_dir/utf8_filename)


if __name__ == "__main__":
    main()
