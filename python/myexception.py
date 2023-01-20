import logging
from typing import Dict

class MyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def check(d: Dict[str, float]) -> None:
    for name, balance in d.items():
        print(name, balance)
        if balance < 2000.0:
            raise MyException('Balance is zero')

def main() -> None:
    logging.basicConfig(filename='bajaj_training/python/logs/logging.log', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug log')
    logger.info('This is an info log')

    b = {
        'Raj': 4000.,
        'Ramesh': 3000.,
        'Mahesh': 1000.,
        'Ram': 4000.
    }

    try:
        check(b)
    except MyException as me:
        print(me)
        logger.exception(me)

if __name__ == '__main__':
    main()