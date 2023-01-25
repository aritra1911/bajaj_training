# Read the file
# Create a dictionary keys should be counts and value is a list of works
# having the same occurrence as key in the given file

from typing import Dict, List, Set
def main() -> None:
    counts: Dict[int, Set[str]] = dict()
    f = open('bajaj_training/python/rev/LICENSE_PYTHON.txt', 'r')
    words: List[str] = f.read().split()
    f.close()

    for word in words:
        count = list(map(lambda word: word.lower(), words)).count(word.lower())
        l = counts.setdefault(count, set())
        l.add(word)

    print(counts)

if __name__ == '__main__':
    main()