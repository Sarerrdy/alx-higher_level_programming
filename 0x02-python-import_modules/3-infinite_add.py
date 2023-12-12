#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
sum = 0
if argc < 2:
    print("{}".format(sum))
else:
    if argc == 2:
        print("{}".format(argv[1]))
    else:
        for n in range(1, argc):
            sum = sum + int(argv[n])
        print(sum)
