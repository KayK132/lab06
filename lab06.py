def encode(digits):  # Kayline Kinda
    result = ""
    for i in digits:
        next = str((int(i) + 3) % 10)
        result += next
    return result

def decode(digits):
    result = ""
    for i in digits:
        next = str((int(i) - 3) % 10)
        result += next
    return result


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # password = None
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

        elif option == 2:
            new_password = encode(password)
            print(f"The encoded password is {new_password}, and the original password is {decode(new_password)}.")

        elif option == 3:
            break

        else:
            print("Invalid option")
        print()

main()