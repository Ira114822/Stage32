from Robot.robot.robot import Robot

class DataConvertor:
    @staticmethod
    def convert_to_string(robots):
        r = "List of robots:\n"
        if not isinstance(robots, (list, tuple)):
            return "List is empty"

        for robot in robots:
            if isinstance(robot, Robot):
                r += "\n" + str(robot)

        return r
