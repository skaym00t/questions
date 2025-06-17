class Flyable:
    def fly(self):
        print("I'm flying!")

class Swimmable:
    def swim(self):
        print("I'm swimming!")

class Duck(Flyable, Swimmable):
    def make_sound(self):
        print('Quack!')

# d = Duck()
# d.fly()
# d.swim()
# d.make_sound()

