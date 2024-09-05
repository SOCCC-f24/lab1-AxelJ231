#!/usr/bin/python3

# Axel Jackson, 138, 9/5/24, CSC

# process
def c2f(c):
    return c * (9 / 5) + 32
# Takes celsius as an input, returns fahrenheit as an output
def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = 100         # input
    print(main(cel))  # output
