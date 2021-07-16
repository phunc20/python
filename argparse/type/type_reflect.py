import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--base", help="the base of an exponential")
parser.add_argument("--power", help="the power or exponent of a number", type=float)
parser.add_argument("--n_students", help="(# students in the classroom)", type=int)
parser.add_argument("--n_teachers", help="(# teachers in the classroom)")
args = parser.parse_args()

print(f"args.base = {args.base}")
print(f"args.power = {args.power}")
print(f"args.n_students = {args.n_students}")
print(f"args.n_teachers = {args.n_teachers}")
print()
print(f"type(args.base) = {type(args.base)}")
print(f"type(args.power) = {type(args.power)}")
print(f"type(args.n_students) = {type(args.n_students)}")
print(f"type(args.n_teachers) = {type(args.n_teachers)}")
