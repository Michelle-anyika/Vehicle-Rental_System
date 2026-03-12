import unittest
from vehicle_rental_system import RentalSystem, Car, Truck, Bike


class TestRentalSystem(unittest.TestCase):
    
    def setUp(self):
        self.system = RentalSystem()
        self.system.add_vehicle(Car("C001", "Toyota", "Camry", 4))
        self.system.add_vehicle(Truck("T001", "Ford", "F-150", 2))
        self.system.add_vehicle(Bike("B001", "Yamaha", "MT-07", "Sport"))
    
    def test_add_vehicle(self):
        system = RentalSystem()
        car = Car("C002", "Honda", "Civic", 4)
        system.add_vehicle(car)
        self.assertIn("C002", system._vehicles)
    
    def test_rent_vehicle_success(self):
        cost, msg = self.system.rent_vehicle("C001", 3)
        self.assertEqual(cost, 150)
        self.assertIn("Successfully rented", msg)
    
    def test_rent_vehicle_not_found(self):
        cost, msg = self.system.rent_vehicle("X999", 3)
        self.assertIsNone(cost)
        self.assertEqual(msg, "Vehicle not found")
    
    def test_rent_already_rented(self):
        self.system.rent_vehicle("C001", 3)
        cost, msg = self.system.rent_vehicle("C001", 2)
        self.assertIsNone(cost)
        self.assertEqual(msg, "Vehicle is already rented")
    
    def test_return_vehicle_success(self):
        self.system.rent_vehicle("C001", 3)
        success, msg = self.system.return_vehicle("C001")
        self.assertTrue(success)
        self.assertEqual(msg, "Vehicle returned successfully")
    
    def test_return_vehicle_not_rented(self):
        success, msg = self.system.return_vehicle("C001")
        self.assertFalse(success)
        self.assertEqual(msg, "Vehicle was not rented")
    
    def test_display_available_vehicles(self):
        result = self.system.display_available_vehicles()
        self.assertIn("C001", result)
        self.assertIn("T001", result)
        self.assertIn("B001", result)
    
    def test_display_all_vehicles(self):
        result = self.system.display_all_vehicles()
        self.assertIn("Toyota", result)
        self.assertIn("Ford", result)
        self.assertIn("Yamaha", result)


if __name__ == '__main__':
    unittest.main()
