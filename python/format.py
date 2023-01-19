def main():
    print("{:5d}".format(12))
    print("{:2d}".format(1234))
    print("{:8.3f}".format(12.2346))
    print("{:05d}".format(12))
    print("{:08.3f}".format(12.2346))
    print("{:^10.3f}".format(12.2346))
    print("{:<05d}".format(12))
    print("{:>08.3f}".format(12.2346))
    print("{:=08.3f}".format(-12.2346))
    print("Hello {} your balance is {}".format("Kapil", 4563))
    print("Hello {name} your balance is {bal}".format(name="Kapil", bal=4563))
    


if __name__ == '__main__':
    main()