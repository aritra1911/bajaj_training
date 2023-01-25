import os
from typing import List, Tuple

def main() -> None:
    text = 'Python is easy to learn . It reduces development time'
    words = text.split()
    n = 2
    #print([ tuple(words[i:i+n]) for i in range(len(words) - n + 1) ])
    print(list(zip(*[words[i:] for i in range(n)])))

if __name__ == '__main__':
    main()