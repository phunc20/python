import random

# tenten is synonyme of dakuten (i.e. ﾞ)
# maru is synonyme of handakuten (i.e. ﾟ)
tenten = "\u3099"
maru = "\u309a"

# hiragana
maruable_hira_ord = [n for n in range(ord("は"), ord("ま"), 3)]
tentenable_hira_ord = [n for n in range(ord("か"), ord("っ"), 2)] + \
                      [n for n in range(ord("つ"), ord("ど"), 2)] + \
                      maruable_hira_ord
maruable_hira = [chr(n) for n in maruable_hira_ord]
tentenable_hira = [chr(n) for n in tentenable_hira_ord]
tenten_hira = [chr(n+1) for n in tentenable_hira_ord]
maru_hira = [chr(n+2) for n in maruable_hira_ord]

# katakana
dist_kana_hira = ord("ア") - ord("あ")
maruable_kana = [chr(n+dist_kana_hira) for n in maruable_hira_ord]
tentenable_kana = [chr(n+dist_kana_hira) for n in tentenable_hira_ord]
tenten_kana = [chr(n+dist_kana_hira+1) for n in tentenable_hira_ord]
maru_kana = [chr(n+dist_kana_hira+2) for n in maruable_hira_ord]

def convert(string, target=tenten):
    if target not in (tenten, maru, ""):
        raise Exception("target arg of convert() should be in (tenten, maru, \"\")")
    converted = [""] * len(string)
    if target == "":
        for i, c in enumerate(string):
            if c in tenten_hira or c in tenten_kana:
                c_converted = chr(ord(c) - 1)
            elif c in maru_hira or c in maru_kana:
                c_converted = chr(ord(c) - 2)
            else:
                c_converted = c
            converted[i] = c_converted
    elif target == tenten:
        for i, c in enumerate(string):
            if c in tentenable_hira or c in tentenable_kana:
                c_converted = chr(ord(c) + 1)
            elif c in maru_hira or c in maru_kana:
                c_converted = chr(ord(c) - 1)
            else:
                c_converted = c
            converted[i] = c_converted
    elif target == maru:
        for i, c in enumerate(string):
            if c in maruable_hira or c in maruable_kana:
                c_converted = chr(ord(c) + 2)
            elif c in tenten_hira or c in tenten_kana:
                c_clean = chr(ord(c) - 1)
                if c_clean in maruable_hira or c_clean in maruable_kana:
                    c_converted = chr(ord(c) + 1)
                else:
                    c_converted = c
            else:
                c_converted = c
            converted[i] = c_converted
    return "".join(converted)


if __name__ == "__main__":
    s = "RWC（実世界情報処理、ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワ。"
    print(f"s                         = {s}")
    print(f"convert(s, target=tenten) = {convert(s, target=tenten)}")
    print(f"convert(s, target=maru)   = {convert(s, target=maru)}")
    print(f"convert(s, target=\"\")     = {convert(s, target='')}")
    print()

    print("Another examplar usage: (Randomly convert)")
    random.seed(42)
    print(f'"".join([convert(c, target=random.choice([tenten, maru, ""])) for c in s]) = {"".join([convert(c, target=random.choice([tenten, maru, ""])) for c in s])}')
