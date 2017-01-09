def get_initials(name):
    name = name.split()
    initials = ''.join(letter[0].upper() for letter in name)
    return(initials)

def main():
    name = input("What is your name?")
    print(get_initials(name))

if __name__ == '__main__':
    main()
