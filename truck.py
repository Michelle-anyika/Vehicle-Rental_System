from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, capacity_tons):
        super().__init__(vehicle_id, brand, model)
        self._capacity_tons = capacity_tons
        self._base_rate = 80

    @property
    def capacity_tons(self):
        return self._capacity_tons

    @property
    def base_rate(self):
        return self._base_rate

    def calculate_rental_cost(self, days):
        return (self._base_rate + self._capacity_tons * 10) * days

    def __str__(self):
        return f"{super().__str__()} - {self._capacity_tons} tons - ${self._base_rate + self._capacity_tons * 10}/day"
