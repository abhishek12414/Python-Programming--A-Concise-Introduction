# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here
src = open(sys.argv[1])
dest = open(sys.argv[2], "w")

for i in src:
    s = str(len(i.strip("\n"))) + "\n"
    dest.write(s)