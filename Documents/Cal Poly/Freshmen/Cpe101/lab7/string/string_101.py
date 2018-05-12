from char import *

def str_rot_13(oldstring):
    newstring = ''
    for ch in oldstring:
        rot_char = char_rot_13(ch)
        newstring = newstring + rot_char
    return newstring

def str_translate_101(word,old,new):
    newstring = ''
    for letter in word:
        if letter == old:
            newstring += new #append
        else:
            newstring += letter
    return newstring
