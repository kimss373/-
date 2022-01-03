from string import ascii_lowercase
from string import ascii_uppercase
import sys
number = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
def check(string):
    lcount = 0
    ucount = 0
    ncount = 0
    mcount = 0
    for i in range(len(string)):
        if string[i] in ascii_lowercase:
            lcount += 1
        elif string[i] in ascii_uppercase:
            ucount += 1
        elif string[i] in number:
            ncount += 1
        elif string[i] == " ":
            mcount += 1
    print(lcount, ucount, ncount, mcount)
while True:
    string = sys.stdin.readline().rstrip("\n")

    if not string:
        break
    check(string)