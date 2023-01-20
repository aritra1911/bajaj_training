import re

def main():
    s = r'This\'; is the: "core" Python\'s book'
    print(re.split(r'\w+', s))

    s = r"She is beautiful"
    print(re.sub(r'beautiful', r'ugly', s))

    s = r"an apple a day keeps the doctor away"
    for w in re.findall(r'a[\w]*', s):
        print(w)

    # print(re.search(r'm\w\w', s).groups())

    s = "one two three four five six seven 8 9 10"
    print(re.findall(r'\b\w{3,5}\b', s))

if __name__ == '__main__':
    main()
