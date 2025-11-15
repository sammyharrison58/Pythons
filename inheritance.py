class animal:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class dog(animal):
    def speak(self):
        return f"{self.name} says Woof!"


class cat(animal):
    def speak(self):
        return f"{self.name} says Meow!"


class mouse(animal):
    def speak(self):
        return f"{self.name} says Squeak!"


dog1 = dog("Buddy")
cat1 = cat("Whiskers")
mouse1 = mouse("Mickey")
print(dog1.speak())
print(cat1.eat())
print(mouse1.sleep())
