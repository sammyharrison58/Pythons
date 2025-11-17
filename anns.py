class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def describe(self):
        return f"This is an animal named {self.name}."


class prey(animal):
    def flee(self):
        return f"{self.name} is fleeing from a predator."


class predator(animal):
    def hunt(self):
        return f"{self.name} is hunting for prey."


class rabbit(prey):
    pass


class fox(predator):
    pass


class fish(prey, predator):
    pass


rabbit1 = rabbit("Bunny")
print(rabbit1.eat())
