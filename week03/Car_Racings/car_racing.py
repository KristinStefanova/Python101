import json
from random import random, seed
import sys


def read_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)

    return data


def write_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


def create_drivers(data):
    return [Driver(dic['name'], Car(
        dic['car'], dic['model'], dic['max_speed'])) for dic in data["people"]]


class Car:
    def __init__(self, car, model, max_speed):
        if (type(car) is not str or type(model) is not str or
                type(max_speed) is not int):
            raise TypeError
        if max_speed < 0:
            raise ValueError
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __int__(self):
        return self.max_speed

    def __str__(self):
        return f'car: {self.car}, model: {self.model}, max speed: {self.max_speed}'

    def __repr__(self):
        return f'{self.car}, model: {self.model}, max speed: {self.max_speed}'

    def __le__(self, other):
        return self.max_speed <= other.max_speed

    def __eq__(self, other):
        return (self.car == other.car and self.model == other.model and
                self.max_speed == other.max_speed)

    def __hash__(self):
        return hash((self.car, self.model, self.max_speed))


class Driver:
    def __init__(self, name, car):
        if type(name) is not str:
            raise TypeError
        if type(car) is not Car:
            raise TypeError
        self.name = name
        self.car = car

    def __str__(self):
        return f'{self.name}, {self.car}'

    def __repr__(self):
        return f'{self.name}, {self.car}'

    def __eq__(self, other):
        return self.name == other.name and self.car == other.car

    def __hash__(self):
        return hash((self.name, self.car))


class Race:
    def __init__(self, drivers, crash_chance):
        if not any([True for driver in drivers if type(driver) is Driver]):
            raise TypeError
        if crash_chance < 0 or crash_chance > 1:
            raise ValueError
        self.drivers = drivers
        self.crash_chance = crash_chance

    def __getitem__(self, index):
        return self.drivers[index]

    def get_racers_by_crash_chance(self):
        seed()
        return [(driver, driver.car.max_speed * self.crash_chance * random())
                for driver in self.drivers]

    def result_help(self):
        scores = self.get_racers_by_crash_chance()
        data = {"result": []}
        counter = 8
        for driver, score in scores:
            if score > (driver.car.max_speed * random()):
                data["result"].append({"name": driver.name, "score": -1})
            elif counter < 4:
                data["result"].append({"name": driver.name, "score": 0})
            else:
                data["result"].append({"name": driver.name, "score": counter})
                counter -= 2
        return data

    def result(self):
        data = self.result_help()
        data["result"] = sorted(data['result'], key=lambda x: x['score'], reverse=True)
        counter = 3
        for dic in data["result"]:
            if counter > 0 and dic["score"] != -1:
                print(f'{dic["name"]} - {dic["score"]}')
                counter -= 1
            else:
                print(f'Unfortunately, {dic["name"]} has crashed.')
                dic["score"] = 0
        write_json('result.json', data)
        return '\n'


class Championship:
    def __init__(self, name, races_count):
        if type(name) is not str:
            raise TypeError
        if type(races_count) is not int:
            raise TypeError
        if races_count < 1:
            raise ValueError
        self.name = name
        self.races_count = races_count

    def make_races(self, _drivers):
        print(f'Starting a new championship called {self.name} with {self.races_count} races.\n')
        print(f'Race #1\n###### START ######')
        seed()
        race = Race(_drivers, random())
        race.result()
        data = read_json('result.json')
        for i in range(1, self.races_count):
            print(f'\nRace #{i + 1}\n###### START ######')
            race = Race(_drivers, random())
            race.result()
            temp_data = read_json('result.json')
            for dic in data["result"]:
                for dd in temp_data["result"]:
                    if dic["name"] == dd["name"]:
                        dic["score"] += dd["score"]
            write_json('result.json', data)
        return '\n'

    def standings(self):
        data = read_json('result.json')
        print('Total championship standings:\n')
        for dic in sorted(
                data['result'], key=lambda x: x['score'], reverse=True):
            if dic['score'] > 0:
                print(f'{dic["name"]} - {dic["score"]}')
            else:
                print(f'{dic["name"]} - 0')
        return '\n'


def main():
    # car_one = Car("Opel", "Astra", 200)
    # car_two = Car("Fiat", "Bravo", 180)
    # car_three = Car("BMW", "d350", 250)
    # car_four = Car("Opel", "Vectra", 220)
    # driver_one = Driver("Kiko", car_one)
    # driver_two = Driver("Sasho", car_two)
    # driver_three = Driver("Andy", car_three)
    # driver_four = Driver("Gabriel", car_four)
    # drivers = [driver_one, driver_two, driver_three, driver_four]
    # race_one = Race(drivers, random())
    # print(race_one.result())
    if len(sys.argv) == 1:
        print("""
Hello PyRacer!
Please, call command with the proper argument:
    $ python3 race.py start <name> <races_count> -> This will start a new
championship with the given name, races count and drivers from cars.json
    $ python3 race.py standings -> This will print the standings
for each championship that has ever taken place.""")
    elif len(sys.argv) == 2:
        champ = Championship("", 3)
        champ.standings()
    else:
        champ = Championship(sys.argv[2], int(sys.argv[3]))
        data = read_json("cars.json")
        champ.make_races(create_drivers(data))
        champ.standings()


if __name__ == '__main__':
    main()
