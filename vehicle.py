from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, model):
        self._vehicle_id = vehicle_id
        self._brand = brand
        self._model = model
        self._is_rented = False

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def is_rented(self):
        return self._is_rented

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    def rent(self):
        if self._is_rented:
            return False
        self._is_rented = True
        return True

    def return_vehicle(self):
        if not self._is_rented:
            return False
        self._is_rented = False
        return True

    def __str__(self):
        status = "Rented" if self._is_rented else "Available"
        return f"{self.__class__.__name__} - {self._brand} {self._model} (ID: {self._vehicle_id}) - {status}"
