from helpers import alphabet_position, rotate_character

def encrypt(message, keyword):
    new_string = ""
    counter = 0
    k = 0
    for letter in message:
        k = (counter % len(keyword))
        if letter.isalpha():
            x = alphabet_position(keyword[k])
            new_letter = rotate_character(letter, x)
            new_string += new_letter
            counter += 1
        else:
            new_string += letter
    return(new_string)

def main():
    message = input("Type a message:")
    keyword = input("Encryption code:")
    print(encrypt(message, keyword))

if __name__ == '__main__':
    main()
