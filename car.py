from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, num_doors):
        super().__init__(vehicle_id, brand, model)
        self._num_doors = num_doors
        self._daily_rate = 50

    @property
    def num_doors(self):
        return self._num_doors

    @property
    def daily_rate(self):
        return self._daily_rate

    def calculate_rental_cost(self, days):
        return self._daily_rate * days

    def __str__(self):
        return f"{super().__str__()} - {self._num_doors} doors - ${self._daily_rate}/day"
