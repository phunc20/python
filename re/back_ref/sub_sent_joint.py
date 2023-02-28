import re

def main():
    punctuations = r'\.,;!?():'

    original_strings = [
        "credits.license all needed.",
        "credits,license,anything!You name it?Oder?",
        "all.sorts?of:punc(tuation)s",
        "all.êsorts?ốf:ăccented(ữhc)íac!",
        f"{punctuations=}",
        "... in year 2020.But the following year,all changed.People in the country...",
        "... bigest earthquake.20 people died from it.",
    ]
    print("original_strings:")
    for s in original_strings:
        print(f'{s}')
        print()
    print()
    print()

    #pattern = rf'([{punctuations}])([A-z0-9])'
    pattern = rf'([{punctuations}])([\w])'
    repl = r'\1 \2'
    replaced_strings = [re.sub(pattern, repl, s) for s in original_strings]
    #replaced_strings = [re.sub(pattern, repl, s, flags=re.UNICODE) for s in original_strings]
    print("replaced_strings:")
    for s in replaced_strings:
        print(f'{s}')
        print()


if __name__ == "__main__":
    main()

