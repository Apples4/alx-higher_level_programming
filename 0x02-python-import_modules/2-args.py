#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 == 0:
        print("{0} arguments.")
    elif len(argv) - 1 == 1:
        print("1 argument")
    else:
        print("{0} arguments".format(len(argv) - 1))
    for x in range(1, len(argv)):
        print("{0}: {1}".format(x, str(argv[x])))
