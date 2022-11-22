from Robot.robot.robot import Robot
from Robot.util.creator import RobotCreator

class RobotManager:
    @staticmethod
    def calculate_total_coast(robots):
        total_coast = 0
        if not isinstance(robots, (list, tuple)):
            return -1

        for robot in robots:
             if isinstance(robot, Robot):
                total_coast += robot.price

        return total_coast

    @staticmethod
    def find_max_intelligence_level(robots):
        max_level = 0
        if not isinstance(robots, (list, tuple)):
            return -1

        for robot in robots:
            if isinstance(robot, Robot):
                if robot.intelligence_level > max_level:
                    max_level = robot.intelligence_level

        return max_level
