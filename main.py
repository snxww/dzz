class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety - 100
                return

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
            self.money += set.job.salary
            self.gladness += self.job.gladness_less
            self.satiety -= 4

    def shopping(self):
        if self.satiety():
            pass
        else:
            if self.money < 5:
                self.job('go to work')

    def chill(self):
        if self.gladness():
            pass
        else:
            if self.gladness():
                self.job('go to wo')

    def clear_home(self):
        if self.chill():
            pass
        else:
            self.home = 50
            self.clear_home('clear home pls')

    def to_repair(self):
        if self.car():
            pass
        else:
            self.car = 5
            self.car('repair me')

    def indexes_day(self, day):
        pass

    def is_alive(self):
        if self.gladness:
            pass
        else:
            self.money = 0
            self.job('go to work')

    def live(self):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move....')
            return False


class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {'Java': {'salary': 50, "gladness_less": 10},
            'C++': {'salary': 80, "gladness_less": 5},
            'Python': {'salary': 30, "gladness_less": 8},
            'Rust': {'salary': 60, "gladness_less": 6}}

brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 15},
                'Lada': {'fuel': 70, 'strength': 20, 'consumption': 8},
                'Volvo': {'fuel': 90, 'strength': 150, 'consumption': 6},
                'Ford': {'fuel': 50, 'strength': 120, 'consumption': 12}}
print(brand_of_car.keys())
print(list(brand_of_car))
