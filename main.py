def main():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                print("Radius must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    circle = Circle(radius)

    print(f"Diameter: {circle.calculate_diameter()}")
    print(f"Circumference: {circle.calculate_circumference()}")
    print(f"Area: {circle.calculate_area()}")

    while True:
        grow_choice = input("Do you want the circle to grow? (yes/no): ").lower()
        if grow_choice == "yes":
            circle.grow()
            print("Circle has grown.")
            print(f"New Radius: {circle.get_radius()}")
            print(f"New Diameter: {circle.calculate_diameter()}")
            print(f"New Circumference: {circle.calculate_circumference()}")
            print(f"New Area: {circle.calculate_area()}")
        elif grow_choice == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()