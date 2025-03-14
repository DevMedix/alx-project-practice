#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    
    count = 0
    for index, argument in enumerate(argv[1:], start=1):
        count += int(argument)
    print(count)