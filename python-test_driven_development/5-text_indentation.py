#!/usr/bin/python3

def text_indentation(text):
    space = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if space:
            if text[i] != " ":
                space = False
            continue
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            if i + 1 < len(text) - 1:
                if text[i + 1] == " ":
                    space = True
