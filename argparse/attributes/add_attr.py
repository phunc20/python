import argparse
#import pprint
#pp = pprint.PrettyPrinter()
#pprint = pp.pprint

parser = argparse.ArgumentParser()
parser.add_argument("--power", help="the power or exponent of a number", type=float)
parser.add_argument("--n_students", help="(# students in the classroom)", type=int)
args = parser.parse_args()

def non_dunder(sth):
    return [s for s in dir(sth) if not s.startswith("__")]

print(f"type(parser) = {type(parser)}")
print(f"type(args) = {type(args)}")
print()
print(f"non_dunder(args) = {non_dunder(args)}")
print()
print("""
===============================================================
Add two more attributes to args: another_attr, yet_another_attr
===============================================================
""")
args.another_attr = "rubbish"
args.yet_another_attr = {
    "width": 500,
    "height": 700,
}
print(f"args.another_attr = {args.another_attr}")
print(f"args.yet_another_attr = {args.yet_another_attr}")
print(f"args.power = {args.power}")
print(f"args.n_students = {args.n_students}")
print()
print(f"type(args.another_attr) = {type(args.another_attr)}")
print(f"type(args.yet_another_attr) = {type(args.yet_another_attr)}")
print(f"type(args.power) = {type(args.power)}")
print(f"type(args.n_students) = {type(args.n_students)}")
print()
print(f"non_dunder(args) = {non_dunder(args)}")

