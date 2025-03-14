#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_of_args = len(argv) - 1
    if num_of_args == 0:
        print("0 argument.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print(f"{num_of_args} arguments:")
    
    for index, argument in enumerate(argv[1:], start=1):
        print(f"{index}: {argument}")