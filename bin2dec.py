import re

def main():
    while True:
        bi = input("Put a number in base 2: ")
        matches = re.search(r"^[01]{8}$", bi)
        if matches:
            break
        else:
            print("Invalid number")
            pass
    print(convert_to_dec(bi))


def convert_to_dec(x):
    dec = 0
    array = list(x)
    for i in range(len(array)):
        dec = dec + int(array[i]) * 2 ** (len(array) - i - 1)
    return dec




if __name__ == "__main__":
    main()