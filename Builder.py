# Builder
class Builder(object):
    def build_body(self):
        raise NotImplementedError()

    def build_under_hood(self):
        raise NotImplementedError()

    def build_driving_part(self):
        raise NotImplementedError()

    def create_car(self):
        raise NotImplementedError()


class Car(object):
    def __init__(self, body, under_hood, driving_part):
        self._body = body
        self._under_hood = under_hood
        self._driving_part = driving_part
        self._brains = False  # Взаимодействие функционала машины - подкапотное <--> мозги

    def ready(self):
        self._brains = True

    def not_ready(self):
        self._brains = False

    def __str__(self):
        brains = 'ready' if self._brains else 'not_ready'
        return f'Brains is {brains}. You could use the car functionality'


class Body(object):
    """Кузов"""


class UnderHood(object):
    """Подкапотное пространство"""


class DrivingPart(object):
    """Элементы ходовой"""


class CarBuilder(Builder):
    def build_body(self):
        return Body()

    def build_under_hood(self):
        return UnderHood()

    def build_driving_part(self):
        return DrivingPart()

    def create_car(self):
        body = self.build_body()
        under_hood = self.build_under_hood()
        driving_part = self.build_driving_part()
        return Car(body, under_hood, driving_part)


my_builder = CarBuilder()

my_car = my_builder.create_car()
my_car.ready()
print(my_car)
