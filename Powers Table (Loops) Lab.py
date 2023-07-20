def print_table(n):
    print("Number  Squared Cubed")
    print("======  ======= =====")
    for i in range(1, n + 1):
        print(f"{i:6} {i ** 2:7} {i ** 3:5}")

def print_multiplication_table(n):
    print("\nMultiplication Table:")
    print("   ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print()
    print("   =", "=" * (n * 4))
    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()

def main():
    print("Learn your squares and cubes!")
    while True:
        try:
            num = int(input("\nEnter an integer: "))
            print_table(num)
            continue_choice = input("\nContinue? (y/n): ")
            if continue_choice.lower() != "y":
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    extended_challenge_choice = input("\nDo you want to see the multiplication table? (y/n): ")
    if extended_challenge_choice.lower() == "y":
        while True:
            try:
                table_size = int(input("\nEnter the size of the multiplication table: "))
                print_multiplication_table(table_size)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")


