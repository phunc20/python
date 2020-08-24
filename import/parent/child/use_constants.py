import sys
import os
print(f"(Before) sys.path = {sys.path}")
print()

## useless
#sys.path.append("..")
## 2nd attempt
sys.path.append(os.path.abspath(os.path.pardir))

print(f"(After) sys.path = {sys.path}")
print()

## error
#from colab import constants
import constants
print(f"constants.width = {constants.width}")
