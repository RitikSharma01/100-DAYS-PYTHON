class Animal:
    def __init__(self):
        self.number_eyes = 2

    def heart(self):
        print("fill will kindness")


class dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print('barking')


lucy = dog()
lucy.bark()
lucy.heart()
print(lucy.number_eyes)
