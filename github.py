def main():
    encode_running = True
    menu = 'Menu \n------------- \n1. Encode  \n2. Decode  \n3. Quit'
    print(menu)
    while encode_running:
        choice = input("\nPlease enter an option: ")
        if choice == "1":
            encoding = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            new = encode(encoding)  # storing the encoded password
            print(menu)
        elif choice == "2":
            print(f'The encoded password is {new}, and the original password is {decode(new)}.\n')
            print(menu)
        elif choice == "3":
            encode_running = False


def encode(encoding):
    encoded = ""
    for num in encoding:
        new_digit = str(((int(num) + 3) % 10))  # adds 3 to the number inputted and makes not more than one digit
        encoded += new_digit
    return encoded


def decode(encoding):
    decoder = []
    for i in range(len(encoding)):
        num = encoding[i]
        num = int(num)
        num = num - 3
        if num < 0:
            decoder.append("0")
        else:
            num = str(num)
            decoder.append(num)
    return "".join(decoder)

if __name__ == "__main__":
    main()