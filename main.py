from car import Car
from truck import Truck
from bike import Bike
from rental_system import RentalSystem


def main():
    system = RentalSystem()

    # Add vehicles
    system.add_vehicle(Car("C001", "Toyota", "Camry", 4))
    system.add_vehicle(Car("C002", "Honda", "Civic", 4))
    system.add_vehicle(Truck("T001", "Ford", "F-150", 2))
    system.add_vehicle(Truck("T002", "Chevrolet", "Silverado", 3))
    system.add_vehicle(Bike("B001", "Yamaha", "MT-07", "Sport"))
    system.add_vehicle(Bike("B002", "Harley-Davidson", "Street 750", "Cruiser"))

    print("=== Vehicle Rental System ===\n")
    
    print("All Vehicles:")
    print(system.display_all_vehicles())
    print("\n" + "="*50 + "\n")

    # Rent some vehicles
    print("Renting vehicles:")
    cost, msg = system.rent_vehicle("C001", 3)
    print(f"Car C001: {msg}")
    
    cost, msg = system.rent_vehicle("T001", 5)
    print(f"Truck T001: {msg}")
    
    cost, msg = system.rent_vehicle("B001", 2)
    print(f"Bike B001: {msg}")
    print("\n" + "="*50 + "\n")

    print("Available Vehicles:")
    print(system.display_available_vehicles())
    print("\n" + "="*50 + "\n")

    # Return a vehicle
    print("Returning vehicle:")
    success, msg = system.return_vehicle("C001")
    print(f"Car C001: {msg}")
    print("\n" + "="*50 + "\n")

    print("Available Vehicles After Return:")
    print(system.display_available_vehicles())


if __name__ == "__main__":
    main()
