from typing import List, Tuple

def avg(l: List[int]) -> Tuple[int, float]:
    t = sum(l)
    avg = t / len(l)
    return t, avg

def main():
    try:
        t, a = avg([ int(x) for x in input().split() ])
        print(f'Total = {t}, Average = {avg}')
    except TypeError as te:
        print(te)
    except ZeroDivisionError as ze:
        print(ze)

if __name__ == '__main__':
    main()