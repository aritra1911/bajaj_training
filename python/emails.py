import re

def main():
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_mess = ''
    with open('bajaj_training/python/email_mess.txt') as file:
        email_mess = file.read()

    print(re.findall(email_regex, email_mess))

if __name__ == '__main__':
    main()