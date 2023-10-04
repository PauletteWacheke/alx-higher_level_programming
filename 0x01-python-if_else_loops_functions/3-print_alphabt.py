#!/usr/bin/python3
print("".join(
    "{}".format(chr(c)) for c in range(ord('a'), ord('z') + 1) if chr(c) not in
    'qe'), end="")
