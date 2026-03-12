# Vehicle Rental System

A Python-based vehicle rental system demonstrating OOP principles including inheritance, polymorphism, and abstract base classes.

## Features

- Abstract base class `Vehicle` with common properties and methods
- Three vehicle types: `Car`, `Truck`, and `Bike`
- Dynamic rental cost calculation based on vehicle type and duration
- State management for vehicle availability
- Property decorators for encapsulation

## Project Structure

```
Vehicle-Rental-System/
├── vehicle.py          # Abstract base class
├── car.py             # Car implementation
├── truck.py           # Truck implementation
├── bike.py            # Bike implementation
├── rental_system.py   # Rental management system
├── main.py            # Demo application
└── README.md          # Documentation
```

## Pricing

- **Car**: $50/day
- **Truck**: $80/day + $10/day per ton capacity
- **Bike**: $20/day

## Usage

Run the demo:
```bash
python main.py
```

## Classes

### Vehicle (ABC)
Base abstract class with:
- Properties: vehicle_id, brand, model, is_rented
- Methods: rent(), return_vehicle(), calculate_rental_cost() (abstract)

### Car
Inherits from Vehicle with num_doors attribute

### Truck
Inherits from Vehicle with capacity_tons attribute and capacity-based pricing

### Bike
Inherits from Vehicle with bike_type attribute

### RentalSystem
Manages vehicle inventory and rental operations:
- add_vehicle()
- rent_vehicle()
- return_vehicle()
- display_available_vehicles()
- display_all_vehicles()
