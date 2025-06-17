from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name: str = 'Bird'):
        self.name = name

    @abstractmethod
    def say(self):
        """Какой звук издаёт"""
        pass

    @abstractmethod
    def move(self):
        """Как перемещается в пространстве и времени))"""
        pass

class Sparrow(Bird):
    def say(self):
        return "Чик-чирик!"

    def move(self):
        return f"{self.name} летает"


class Penguin(Bird):
    def say(self):
        return "Громкий крик!"

    def move(self):
        return f"{self.name} плавает и ходит вразвалочку"

s = Sparrow('Воробей Аркадий')
p = Penguin('Пингвин Тиабалду')

def bird_activity(bird: Bird):
    print(f'{bird.move()}, а ещё издаёт звук: {bird.say()}')

birds = [s, p]

for bird in birds:
    bird_activity(bird)