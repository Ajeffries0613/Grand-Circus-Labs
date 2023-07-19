# Create lists with student information
names = ["Sophia Petrillo", "Rose Nylund", "Blanche Devereaux", "Dorothy Zbornak"]
hometowns = ["Sicily", "New York", "Atlanta", "Chicago"]
favorite_foods = ["pizza", "cupcakes", "pasta", "tacos"]


# Function to prompt the user for a valid category
def get_valid_category():
    while True:
        category = input("Enter the category to display (Hometown or Favorite Food): ").lower()
        if category == "hometown" or category == "favorite food":
            print(category)
        else:
            print("Invalid category. Please try again.")

# Function to prompt the user for student information
def get_student_info():
    while True:
        try:
# Prompt user for student number
            student_num = int(input(f"Which student would you like to learn about? Enter a number 1-{len(names)}: "))
            if student_num < 1 or student_num > len(names):
                raise ValueError("Invalid student number.")
            student_index = student_num - 1
# Print student's name
            print("Student's name:", names[student_index])

# Prompt user for category choice
            category = get_valid_category()
            if category == "hometown":
                print("Hometown:", hometowns[student_index])
            elif category == "favorite food":
                print("Favorite food:", favorite_foods[student_index])

# Prompt user if they want to learn about another student
            choice = input("Would you like to learn about another student? Enter 'y' or 'n': ").lower()
            if choice != "y":
                print("Thanks!")