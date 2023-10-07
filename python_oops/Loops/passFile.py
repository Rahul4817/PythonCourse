import os
from random import randint


pas=input("Enter password")
key=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
     's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
     '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

pwg=""

while (pwg!=pas):
    pwg=""
    for i in range(len(pas)):
        guessPas=key[randint(0,4)]
        pwg=str(guessPas)+str(pwg)
        # print(pwg)
        print("gussing....please wait")
        os.system("cls")
print(f"The pass is {pwg}")

1234