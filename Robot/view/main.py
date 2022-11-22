from Robot.robot.robot import Robot
from Robot.robot.manager import RobotManager
from Robot.util.creator import RobotCreator
from Robot.util.convector import DataConvertor


def main():


    robots = RobotCreator.create(7)

    print(DataConvertor.convert_to_string(robots))

    total = RobotManager.calculate_total_coast(robots)
    print(f"\nTotal price: ${total}")

    more_intelligent_robots = RobotManager.find_max_intelligence_level(robots)
    print("\nMore intelligent level: ", more_intelligent_robots)

    print("\nHow many robots have been created?")
    print(Robot.get_created_robots())

if __name__ == "__main__":
    main()
