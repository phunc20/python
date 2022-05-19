"""
This is meant to be a terminal program aiming to aid beginner Japanese learners to pronounce words.

Example:

$ python romajiize.py "1846年、ニューヨークに到着して病院を開業した。" "1892年10月22日、妻の病気を理 
由に離日。"
1846年、ニューヨークに到着して病院を開業した。
1846 nen, nyuuyooku ni touchaku shite byouin wo kaigyou shita.

1892年10月22日、妻の病気を理由に離日。
1892 nen 10 gatsu 22 nichi, tsuma no byouki wo riyuu ni rijitsu.
"""
import argparse
import pykakasi


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "texts",
        help="text to be romaji-ized",
        nargs="+",
        #type=str,
    )
    args = parser.parse_args()
    texts = args.texts
    
    kks = pykakasi.kakasi()
    for i, text in enumerate(texts):
        new_tokens = []
        for transliteration in kks.convert(text):
            hepburn = transliteration["hepburn"]
            new_tokens.append(hepburn)
        romajiized = " ".join(new_tokens)
        print(text)
        print(romajiized)
        if i < len(texts) - 1:
            print()
