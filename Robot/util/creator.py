from Robot.robot.robot import Robot

import random


class RobotCreator:
    @staticmethod
    def create(size):
        NAME = ("Optimus Prime", "T", "Android", "Jetfire", "Vector Prime", "Landmine",
                " Red Alert", "Cobybot", "Quickmix")

        MODEL = ("3.2", "5.0", "1.2", "3000", "800", "1000", "2.0", "5000")

        MIN_LEVEL = 0
        MAX_LEVEL = 100

        MIN_PRICE = 1
        MAX_PRICE = 5_000_000

        ls = []

        for _ in range(size):
            name = random.choice(NAME)
            model = random.choice(MODEL)
            intelligence_level = random.randint(MIN_LEVEL, MAX_LEVEL)
            price = random.randint(MIN_PRICE, MAX_PRICE)

            robot = Robot(name, model, intelligence_level, price)

            ls.append(robot)

        return ls

