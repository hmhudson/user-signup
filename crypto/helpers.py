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
