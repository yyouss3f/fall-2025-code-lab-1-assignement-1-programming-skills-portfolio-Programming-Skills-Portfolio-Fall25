def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break 
        except ValueError:
            print("Please enter a valid number.\n")

    message = check_even_odd(num)
    print(message)

main()