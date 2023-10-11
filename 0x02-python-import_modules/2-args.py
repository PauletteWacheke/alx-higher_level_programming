#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numargs = len(sys.argv) - 1
    if numargs == 0:
        print("0 arguments.")
    elif numargs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numargs))
    for n in range(numargs):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
