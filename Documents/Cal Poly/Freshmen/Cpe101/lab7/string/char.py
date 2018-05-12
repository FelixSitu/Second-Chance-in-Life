def is_lower_101(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False

def is_capital_101(char):
    if ord(char)>= 65 and ord(char) <= 90:
        return True
    else:
        return False

def char_rot_13(char):
    if is_lower_101(char) == True:
        offset = ord('a')
        shifted = ord(char) - offset
        rot_shift = (shifted + 13)%26
        return chr(rot_shift + offset)
    elif is_capital_101(char) == True:
        offset = ord('A')
        shifted = ord(char) - offset
        rot_shift = (shifted + 13) % 26
        return chr(rot_shift + offset)
