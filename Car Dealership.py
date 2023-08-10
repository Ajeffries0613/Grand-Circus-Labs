class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False
    
    def start_engine(self):
        print("Starting engine...")
        self.engine_on = True
    
    def make_noise(self):
        print("Beep beep!")
    

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False
    
    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True
    

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed
    
    def make_noise(self):
        print("Vroom vroom!")


def main():
    print("Hello\nWelcome to GC Bikes & Trucks!")
    
    bikes = [
        Motorcycle("Harley", 0, 50000, 300),
        Motorcycle("Ducati", 1000, 50000, 250),
        Motorcycle("Honda", 2000, 50000, 240)
    ]
    
    trucks = [
        Truck("Toyota", 10000, 30000),
        Truck("Ford", 200000, 5000),
        Truck("Chevy", 50000, 20000)
    ]
    
    vehicles_to_compare = []
    
    while True:
        print("\nWould you like to view bikes or trucks? (b or t)")
        choice_category = input("Enter your choice: ")
        
        if choice_category.lower() == 'b':
            print("\nAvailable Bikes:")
            for idx, bike in enumerate(bikes, start=1):
                print(f"{idx}: {bike.make}")
            selected = int(input("Select a bike to add for comparison: "))
            if 1 <= selected <= len(bikes):
                vehicles_to_compare.append(bikes[selected - 1])
        elif choice_category.lower() == 't':
            print("\nAvailable Trucks:")
            for idx, truck in enumerate(trucks, start=1):
                print(f"{idx}: {truck.make}")
            selected = int(input("Select a truck to add for comparison: "))
            if 1 <= selected <= len(trucks):
                vehicles_to_compare.append(trucks[selected - 1])
        else:
            print("Invalid choice. Please enter 'b' for bikes or 't' for trucks.")
            continue
        
        compare_choice = input("Do you want to add another vehicle to compare? (yes/no): ")
        if compare_choice.lower() != 'yes':
            break
    
    print("\nComparing selected vehicles:")
    for vehicle in vehicles_to_compare:
        print(f"{vehicle.make} - Miles: {vehicle.miles}, Price: {vehicle.price}")
        vehicle.start_engine()
        vehicle.make_noise()


if __name__ == "__main__":
    main()