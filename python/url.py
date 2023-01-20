from urllib.request import urlopen
from typing import Tuple, List

def read_data(url: str) -> None:
    if url.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(url).read().decode('utf-8')
    raise ValueError('Invalid URL!!')

def choose_fields(fields: List[str], choice: Tuple[int]) -> List[str]:
    ret_fields = list()
    for idx in choice:
        ret_fields.append(fields[idx])
    return ret_fields

def main():
    url = r'https://raw.githubusercontent.com/tokern/piicatcher/master/tests/samples/sample-data.csv'
    data = read_data(url)
    lines = data.split('\r\n')
    header = lines[0]
    records = lines[1:-1]
    col_indexes = (0, 1, 2, 4, 5)
    
    with open('bajaj_training/python/data.csv', 'w') as csv_file:
        csv_file.write(','.join(choose_fields(header.split(','), choice=col_indexes)) + '\r\n')
        for record in records:
            csv_file.write(','.join(choose_fields(record.split(','), choice=col_indexes)) + '\r\n')


if __name__ == '__main__':
    main()