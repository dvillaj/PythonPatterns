import abc

class Duck(abc.ABC):

    def _setFlyBehavior(self, flyBehavior):
        self._flyBehavior = flyBehavior

    def _setQuackBehavior(self, quackBehavior):
        self._quackBehavior = quackBehavior

    @abc.abstractmethod
    def display(self):
        pass


    def performFly(self):
        self._flyBehavior.fly()

    def performQuack(self):
        self._quackBehavior.quack()


    def swim(self):
        print("All ducks float, even decoys!")



class Quack:
    def quack(self):
        print("Quack")

class Squeak:
    def quack(self):
        print("Squeak")

class FakeQuack:
    def quack(self):
        print("Qwak")

class MuteQuack:
    def quack(self):
        print("<< silence >>")


class FlyNoWay:
    def fly(self):
        print("I can't fly")

class FlyRocketPowered:
    def fly(self):
        print("I'm flying with a rocket")

class FlyWithWings:
    def fly(self):
        print("I'm flying")




class MallardDuck(Duck):
    def __init__(self):
        super()._setFlyBehavior(FlyWithWings())
        super()._setQuackBehavior(Quack())

    def display(self):
        print("I am a Mallard Decoy")


class ModelDuck(Duck):
    def __init__(self):
        super()._setFlyBehavior(FlyNoWay())
        super()._setQuackBehavior(Quack())

    def display(self):
        print("I am a model Duck")


class RedHeadDuck(Duck):
    def __init__(self):
        super()._setFlyBehavior(FlyWithWings())
        super()._setQuackBehavior(Quack())

    def display(self):
        print("I'm a real Red Headed duck")




class DecoyDuck(Duck):
    def __init__(self):
        super()._setFlyBehavior(FlyNoWay())
        super()._setQuackBehavior(MuteQuack())

    def display(self):
        print("I am a duck Decoy")




class RubberDuck(Duck):
    def __init__(self):
        super()._setFlyBehavior(FlyNoWay())
        super()._setQuackBehavior(Squeak())

    def display(self):
        print("I am a rubber duckie")





duck = DecoyDuck()


duck.display()
duck.swim()
duck.performFly()
duck.performQuack()
