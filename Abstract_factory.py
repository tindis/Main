class CarTypes(object):
    def create_sedan(self):
        raise NotImplementedError()

    def create_hatchback(self):
        raise NotImplementedError()


class Sedan:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    def __str__(self):
        return f"{self._brand} {self._model}"


class Hatchback:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    def __str__(self):
        return f"{self._brand} {self._model}"


class Volkswagen(CarTypes):
    def create_sedan(self):
        return Sedan('Volkswagen', 'Jetta')

    def create_hatchback(self):
        return Hatchback('Volkswagen', 'Polo')


class Toyota(CarTypes):
    def create_sedan(self):
        return Sedan('Toyota', 'Camry')

    def create_hatchback(self):
        return Hatchback('Toyota', 'Prius')


def get_fact(ident):
    if ident == 1:
        return Volkswagen()
    elif ident == 2:
        return Toyota()


fact = get_fact(1)
print(fact.create_sedan())
print(fact.create_hatchback())
