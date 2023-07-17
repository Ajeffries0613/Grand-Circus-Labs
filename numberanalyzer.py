user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

num = int(input("Enter an integer between 1 and 100 inclusive: "))

if num % 2 == 1 and num < 60:
    print(f"{num} is Odd and less than 60.")
elif num % 2 == 0 and 2 <= num <= 24:
    print("Even and less than 25.")
elif num % 2 == 0 and 26 <= num <= 60:
    print("Even and between 26 and 60 inclusive.")
elif num % 2 == 0 and num > 60:
    print(f"{num} is Even and greater than 60.")
elif num % 2 == 1 and num > 60:
    print(f"{num} is Odd and greater than 60.")
if input("Do you want to continue? (y/n): ").lower() != 'y':
    print(f"Goodbye {user_name}!")


