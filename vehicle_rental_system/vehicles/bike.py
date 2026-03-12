from .vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, bike_type):
        super().__init__(vehicle_id, brand, model)
        self._bike_type = bike_type
        self._daily_rate = 20

    @property
    def bike_type(self):
        return self._bike_type

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if value < 0:
            raise ValueError("Daily rate cannot be negative")
        self._daily_rate = value

    def calculate_rental_cost(self, days):
        return self._daily_rate * days

    def __str__(self):
        return f"{super().__str__()} - {self._bike_type} - ${self._daily_rate}/day"
