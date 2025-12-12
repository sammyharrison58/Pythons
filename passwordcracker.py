from random import *
import os

your_password = input("enter your password:")
pwd = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "1",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
pw = ""
while pw != your_password:
    pw = ""
    for letter in range(len(your_password)):
        guess_pwd = pwd[randint(0, 17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("cracking password...please wait")
        os.system("cls")
print("Your password is:", pw)
