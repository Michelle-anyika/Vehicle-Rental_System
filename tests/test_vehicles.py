import unittest
from vehicle_rental_system import Car, Truck, Bike


class TestVehicles(unittest.TestCase):
    
    def test_car_creation(self):
        car = Car("C001", "Toyota", "Camry", 4)
        self.assertEqual(car.vehicle_id, "C001")
        self.assertEqual(car.brand, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.num_doors, 4)
        self.assertFalse(car.is_rented)
    
    def test_car_rental_cost(self):
        car = Car("C001", "Toyota", "Camry", 4)
        self.assertEqual(car.calculate_rental_cost(3), 150)
    
    def test_car_daily_rate_setter(self):
        car = Car("C001", "Toyota", "Camry", 4)
        car.daily_rate = 60
        self.assertEqual(car.daily_rate, 60)
        self.assertEqual(car.calculate_rental_cost(2), 120)
    
    def test_truck_creation(self):
        truck = Truck("T001", "Ford", "F-150", 2)
        self.assertEqual(truck.capacity_tons, 2)
        self.assertEqual(truck.calculate_rental_cost(1), 100)
    
    def test_truck_base_rate_setter(self):
        truck = Truck("T001", "Ford", "F-150", 2)
        truck.base_rate = 100
        self.assertEqual(truck.calculate_rental_cost(1), 120)
    
    def test_bike_creation(self):
        bike = Bike("B001", "Yamaha", "MT-07", "Sport")
        self.assertEqual(bike.bike_type, "Sport")
        self.assertEqual(bike.calculate_rental_cost(2), 40)
    
    def test_rent_vehicle(self):
        car = Car("C001", "Toyota", "Camry", 4)
        self.assertTrue(car.rent())
        self.assertTrue(car.is_rented)
        self.assertFalse(car.rent())
    
    def test_return_vehicle(self):
        car = Car("C001", "Toyota", "Camry", 4)
        car.rent()
        self.assertTrue(car.return_vehicle())
        self.assertFalse(car.is_rented)
    
    def test_is_rented_setter(self):
        car = Car("C001", "Toyota", "Camry", 4)
        car.is_rented = True
        self.assertTrue(car.is_rented)
        car.is_rented = False
        self.assertFalse(car.is_rented)


if __name__ == '__main__':
    unittest.main()
