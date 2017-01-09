from sys import argv, exit

from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    rot_message = ""
    for i in text:
        if i.isalpha():
            x = rotate_character(i, rot)
            rot_message += str(x)
        else:
            rot_message += str(i)
    return(rot_message)

def user_input_is_valid(cl_args):
    if len(cl_args) != 2:
        return False
    if cl_args[1].isdigit()== True:
        return True
    else:
        return False

def main():
    if user_input_is_valid(argv) == False:
        print("usage: python3 caesar.py n")
        exit()
    text = input("Type a message:")
    rot = int(argv[1])
    user_input_is_valid(argv)
    print(encrypt(text, rot))

if __name__ == '__main__':
    main()
