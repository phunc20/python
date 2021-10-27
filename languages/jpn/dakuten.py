import unicodedata

# tenten is synonyme of dakuten (i.e. ﾞ)
# maru is synonyme of handakuten (i.e. ﾟ)
tenten = "\u3099"
maru = "\u309a"

def is_hira(char):
    """
    Note. strings like "\u3041" denotes hexadecimal (uni)code.
    As a consequence, in the range ["\u3041" .. "\u3096"], there
    are 5*16 + 5 + 1 = 86 code points.
    """
    if len(char) != 1:
        raise Exception("The input to is_hira() should be a length-1 string")
    return "\u3041" <= char <= "\u3096"

def is_kana(char):
    """
    There are therefore 5*16 + 6 + 1 = 87 katakana characters.
    """
    if len(char) != 1:
        raise Exception("The input to is_kana() should be a length-1 string")
    return "\u30a1" <= char <= "\u30f7"

def has_tenten_maru(char, nfd=None):
    """
    """
    if len(char) != 1:
        raise Exception("The input to has_tenten_maru() should be a length-1 string")
    if not nfd:
        nfd = unicodedata.normalize("NFD", char)
    if len(nfd) == 1:
        return False
    else:
        suspect = nfd[1]
        if suspect == tenten or suspect == maru:
            return suspect
        else:
            return False

def flip(string, target=tenten):
    flipped = [""] * len(string)
    for i, c in enumerate(string):
        if not is_hira(c) and not is_kana(c):
            c_flipped = c
        else:
            nfd = unicodedata.normalize("NFD", c)
            mark = has_tenten_maru(c, nfd)
            if not mark:
                c_flipped = unicodedata.normalize("NFC", c + target)
            else:
                if mark == target:
                    c_flipped = nfd[0]
                else:
                    c_flipped = c
        flipped[i] = c_flipped
    return "".join(flipped)


if __name__ == "__main__":
    #s = "HLAC特徴を用いた学習型汎用認識"
    s = "また著者も国のRWC（実世界情報処理）プロジェクトで忙しく、その後注目されずにいた。"
    print(f"s                      = {s}")
    print(f"flip(s, target=tenten) = {flip(s, target=tenten)}")
    print(f"flip(s, target=maru)   = {flip(s, target=maru)}")
    print(f"flip(flip(s), maru)    = {flip(flip(s), maru)}")
