class Animal(object):
    def __init__(self, name: str):
        self.name = name

    def display_info(self):
        return self.name


class Lion(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name

class Bear(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name

class Tiger(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.name=name

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def add_bear(self, name):
        self.animals.append(Bear(name))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("bear1")
zoo1.add_bear("bear2")
zoo1.print_all_info()