# Given a string s1, write a program to return the sum and average of the digits that
# appear in the string, ignoring all other characters
 
# str1 = "PythON29@#8496"
from statistics import mean

def main() -> None:
    str1 = 'PythON29@#8496'
    nums = [ int(c) for c in str1 if c.isnumeric() ]
    print('sum =', sum(nums), '\navg =', mean(nums))

if __name__ == '__main__':
    main()