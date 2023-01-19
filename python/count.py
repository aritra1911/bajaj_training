def main():
    s = "I am learning python"
    s = s.lower()
    for char in list(set(s)):
        if char == ' ': continue
        count = len([ c for c in s if char == c ])
        print(char, ':', count)

if __name__ == '__main__':
    main()
