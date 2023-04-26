import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n_students",
                    help="(# students in the class)",
                    type=int,
                    default=32,
)
parser.add_argument("--n_teachers",
                    help="(# teachers in the class)",
                    type=int,
)
parser.add_argument("--store_true",
                    action="store_true",
)
parser.add_argument("--store_false",
                    action="store_false",
)
parser.add_argument("--store_true_default_true",
                    action="store_true",
                    default=True,
)
parser.add_argument("--store_false_default_false",
                    action="store_false",
                    default=False,
)
args = parser.parse_args([])

print(f"args = {args}")
print()
print(f"args.n_students = {args.n_students}")
print(f"args.n_teachers = {args.n_teachers}")
print(f"args.store_true = {args.store_true}")
print(f"args.store_false = {args.store_false}")
print(f"args.store_true_default_true = {args.store_true_default_true}")
print(f"args.store_false_default_false = {args.store_false_default_false}")
print()
print(f"type(args.n_students) = {type(args.n_students)}")
print(f"type(args.n_teachers) = {type(args.n_teachers)}")
print(f"type(args.store_true) = {type(args.store_true)}")
print(f"type(args.store_false) = {type(args.store_false)}")
#print(f"type(args.store_true_default_true) = {type(args.store_true_default_true)}")
#print(f"type(args.store_false_default_false) = {type(args.store_false_default_false)}")
