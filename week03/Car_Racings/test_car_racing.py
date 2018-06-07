import unittest
from car_racing import Car, Driver, Race


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car_one = Car("Opel", "Astra", 200)
        self.car_two = Car("Fiat", "Bravo", 180)
        self.car_three = Car("BMW", "d350", 250)
        self.car_four = Car("Opel", "Vectra", 220)

    def test_car_init(self):
        with self.assertRaises(TypeError):
            Car([], "", 150)
        with self.assertRaises(TypeError):
            Car("", [], 150)
        with self.assertRaises(TypeError):
            Car("", "", "")


class DriverTest(unittest.TestCase):
    def setUp(self):
        self.car_one = Car("Opel", "Astra", 200)
        self.car_two = Car("Fiat", "Bravo", 180)
        self.car_three = Car("BMW", "d350", 250)
        self.car_four = Car("Opel", "Vectra", 220)
        self.driver_one = Driver("Kiko", self.car_one)
        self.driver_two = Driver("Sasho", self.car_two)
        self.driver_three = Driver("Andy", self.car_three)
        self.driver_four = Driver("Gabriel", self.car_four)

    def test_car_init(self):
        with self.assertRaises(TypeError):
            Driver(15, self.car_one)
        with self.assertRaises(TypeError):
            Driver("", [])


class RaceTest(unittest.TestCase):
    def setUp(self):
        self.car_one = Car("Opel", "Astra", 200)
        self.car_two = Car("Fiat", "Bravo", 180)
        self.car_three = Car("BMW", "d350", 250)
        self.car_four = Car("Opel", "Vectra", 220)
        self.driver_one = Driver("Kiko", self.car_one)
        self.driver_two = Driver("Sasho", self.car_two)
        self.driver_three = Driver("Andy", self.car_three)
        self.driver_four = Driver("Gabriel", self.car_four)

    def test_race_init(self):
        with self.assertRaises(TypeError):
            Race(15, self.car_one)
        with self.assertRaises(TypeError):
            Race("", [])

    def test_result(self):
        pass


if __name__ == '__main__':
    unittest.main()
