#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for x in range(len(argv) - 1):
        sum = sum + int(argv[x + 1])
    print('{}'.format(sum))
