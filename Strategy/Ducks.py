class Duck():
    def quack(self):
        print("Quack")

    def swim(self):
        print("Swim")

    def diplay(self):
        print("I am a Duck")


class MallardDuck(Duck):
    def diplay(self):
        print("I am a Mallard Duck")

class RedHeadDuck(Duck):
    def diplay(self):
        print("I am a RedHead Duck")


duck = RedHeadDuck()

duck.swim()
duck.diplay()