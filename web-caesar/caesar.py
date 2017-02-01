import string

def alphabet_position(letter):
    for i in letter:
        if letter.isupper():
            return string.ascii_uppercase.index(letter)
        else:
            return string.ascii_lowercase.index(letter)

def rotate_character(char, rot):
    letter = alphabet_position(char)
    new_letter = ((letter + int(rot)) % 26)
    lower = True
    if char.isupper():
        lower = False
    return_letter = string.ascii_lowercase[new_letter]
    if lower == True:
        return return_letter
    else:
        return return_letter.upper()

def encrypt(text, rot):
    rot_message = ""
    for i in text:
        if i.isalpha():
            x = rotate_character(i, rot)
            rot_message += str(x)
        else:
            rot_message += str(i)
    return(rot_message)
