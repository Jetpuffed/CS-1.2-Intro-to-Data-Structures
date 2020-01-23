import sys
import random

args = sys.argv[1:]

print(*random.sample(args, len(args)))
