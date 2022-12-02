from BasicCarClass import Car

class Garage:

    def __init__(self):
        self._cars =[]

    @property
    def cars(self):
        return self._cars

    @property
    def num_of_cars(self):
        return len(self._cars)

    def add(self, car):
        if isinstance(car, Car):
            if car in self._cars:
                print('Car is already in the garage')
                return
            self._cars.append(car)

    def remove(self, car):
        if isinstance(car, Car) and car in self.cars:
            self._cars.remove(car)

    def clear(self):
        self._cars.clear()

