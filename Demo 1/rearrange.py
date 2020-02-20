#!/usr/bin/env python3
# encoding=utf-8

import random
import sys

args = sys.argv[1:]

print(*random.sample(args, len(args)))
