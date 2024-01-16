#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(i, end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            if text[i + 1] == " ":
                i += 1
