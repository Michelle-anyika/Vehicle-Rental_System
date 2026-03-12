class RentalSystem:
    def __init__(self):
        self._vehicles = {}

    def add_vehicle(self, vehicle):
        self._vehicles[vehicle.vehicle_id] = vehicle

    def rent_vehicle(self, vehicle_id, days):
        if vehicle_id not in self._vehicles:
            return None, "Vehicle not found"
        
        vehicle = self._vehicles[vehicle_id]
        if vehicle.rent():
            cost = vehicle.calculate_rental_cost(days)
            return cost, f"Successfully rented for {days} days. Total cost: ${cost}"
        return None, "Vehicle is already rented"

    def return_vehicle(self, vehicle_id):
        if vehicle_id not in self._vehicles:
            return False, "Vehicle not found"
        
        vehicle = self._vehicles[vehicle_id]
        if vehicle.return_vehicle():
            return True, "Vehicle returned successfully"
        return False, "Vehicle was not rented"

    def display_available_vehicles(self):
        available = [v for v in self._vehicles.values() if not v.is_rented]
        if not available:
            return "No vehicles available"
        return "\n".join(str(v) for v in available)

    def display_all_vehicles(self):
        if not self._vehicles:
            return "No vehicles in system"
        return "\n".join(str(v) for v in self._vehicles.values())
