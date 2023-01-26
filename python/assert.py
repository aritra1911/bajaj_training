def main() -> None:
    x: int = int(input('Enter a number greater than 0'))
    try:
        assert x > 0, 'Wrong input on variable x' 'Wrong value for x'
    except AssertionError as ae:
        print(ae)

# unitTest
# --------
# assertEqual(a, b)     | a == b
# assertNotEqual(a, b)  | a == b
# assertTrue(x)         | bool(x) is True
# assertFalse(x)        | bool(x) si False
# assertIn(x)

if __name__ == '__main__':
    main()