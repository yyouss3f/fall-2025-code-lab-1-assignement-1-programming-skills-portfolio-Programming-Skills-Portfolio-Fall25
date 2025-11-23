

name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number!")

print("Checking information...")
print("_____________________________________")

print("Your full name is : ",name)
print("Your hometown is :", hometown)
print("Your age is :", age)