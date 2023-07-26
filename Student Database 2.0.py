def list_names(students):
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']}")

def get_new_student():
    name = input("Please input a name for the new student:\n> ")
    hometown = input("Next please input their hometown:\n> ")
    favorite_food = input("Last please input their favorite food:\n> ")
    return {"name": name, "hometown": hometown, "favorite_food": favorite_food}

def main():
    students = [
        {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
        {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
        {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
    ]

    while True:
        print("Please select which action you'd like to do: add, view, or quit")
        user_input = input("> ").lower()

        if user_input == "add":
            new_student = get_new_student()
            students.append(new_student)
            print("\nNew student added successfully!\n")

        elif user_input == "view":
            list_names(students)
            print("Which student would you like to learn more about? Enter a number 1-{}:".format(len(students)))
            try:
                index = int(input("> ")) - 1
                selected_student = students[index]
                print("Student {} is {}.".format(index + 1, selected_student["name"]))
                info_type = input("What would you like to know?\nEnter 'hometown' or 'favorite food'\n> ").lower()
                if info_type == "hometown":
                    print("{} is from {}".format(selected_student["name"], selected_student["hometown"]))
                elif info_type == "favorite food":
                    print("{}'s favorite food is {}".format(selected_student["name"], selected_student["favorite_food"]))
                else:
                    print("Invalid input! Please try again.")
            except IndexError:
                print("Invalid index! Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif user_input == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
