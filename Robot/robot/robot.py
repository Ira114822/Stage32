class Robot:
    _count = 0

    def __init__(self, name, model, intelligence_level, price):
        self._name = name
        self._model = model
        self._intelligence_level = intelligence_level
        self._price = price
        Robot._count += 1


    def __str__(self):
        return f"Robot {self._name} {self._model}: " \
               f"\nintelligence level: {self._intelligence_level}" \
               f"\nprice: {self._price}"

    @property
    def name(self):
        print("Robot", self._name, "was create.")
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name_del(self):
        print("Robot", self._name, "was destroyed.")
        del self._name

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @model.deleter
    def model(self):
        del self._model

    @property
    def intelligence_level(self):
        return self._intelligence_level

    @intelligence_level.setter
    def intelligence_level(self, intelligence_level):
        if 100 >= intelligence_level >= 0:
            self._intelligence_level = intelligence_level

    @intelligence_level.deleter
    def intelligence_level(self):
        del self._intelligence_level

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price > 0:
           self._price = price

    @price.deleter
    def price(self):
        del self._price

    def get_created_robots():
        return Robot._count