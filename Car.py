class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.time = 0

    def say_state(self):
        print("I'm going {} kph".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

if __name__ == '__main__':

    my_car = Car()
    while True:
        action = input("[A]ccelerate, [B]rake ").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        my_car.say_state()