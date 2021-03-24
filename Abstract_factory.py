from abc import *


class AutoTypes(ABC):

    @abstractmethod
    def type_description(self):
        pass


class Sedan(AutoTypes):
    name = 'Sedan'

    def type_description(self):
        print(f"This is standard car body configuration - {self.name}")


class Hatchback(AutoTypes):
    name = 'Hatchback'

    def type_description(self):
        print(f"This is car body configuration with a rear door - {self.name}")


class Crossover(AutoTypes):
    name = 'Crossover'

    def type_description(self):
        print(f"This is a type of sport utility vehicle-like vehicle"
              f"built with uni-body frame construction - {self.name}")


class Cars(ABC):

    @abstractmethod
    def get_car(type_of_car):
        pass


class Volkswagen(Cars):

    def get_car(type_of_car):
        if type_of_car == 'Sedan':
            print(f"{type_of_car} in sale: Passat, Arteon, Polo, Jetta")
            return Sedan()
        elif type_of_car == 'Hatchback':
            print(f"{type_of_car}in sale: Golf, Golf Plus, Polo")
            return Hatchback()
        elif type_of_car == 'Crossover':
            print(f"{type_of_car} in sale: Tiguan, Touareg, T-Roc")
            return Crossover()


class Toyota(Cars):
    def get_car(type_of_car):
        if type_of_car == 'Sedan':
            print(f"{type_of_car} in sale: Camry, Corolla, Avalon")
            return Sedan()
        elif type_of_car == 'Hatchback':
            print(f"{type_of_car}in sale: Prius, Prius C, Corolla, Auris")
            return Hatchback()
        elif type_of_car == 'Crossover':
            print(f"{type_of_car} in sale: Prado, Land Cruiser, RAV4, C-HR")
            return Crossover()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "Volkswagen":
            return Volkswagen
        if type_of_factory == "Toyota":
            return Toyota


print(f"Our cars:\n 1. Volkswagen\n 2. Toyota")
fp = FactoryProducer()

fac1 = fp.get_factory("Volkswagen")
sedan_fac1 = fac1.get_car("Sedan")
sedan_fac1.type_description()

hatch_fac1 = fac1.get_car("Hetchback")
hatch_fac1.type_description()

cross_fac1 = fac1.get_car("Hatchback")
cross_fac1.type_description()


fac2 = fp.get_factory("Toyota")
sedan_fac2 = fac2.get_car("Sedan")
sedan_fac2.type_description()

hatch_fac2 = fac2.get_car("Hetchback")
hatch_fac2.type_description()

cross_fac2 = fac2.get_car("Hatchback")
cross_fac2.type_description()
