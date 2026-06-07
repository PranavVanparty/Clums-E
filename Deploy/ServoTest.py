import json
import time

from adafruit_servokit import ServoKit

continuous_servo = True


def main():
    print("This is a test. Will move servo on Channel 0")
    try:
        kit = ServoKit(channels=16)
        if continuous_servo:
            testContinuousServo(kit)
        else:
            testServo(kit)
        kit.continuous_servo[0].fraction = 0

    except KeyboardInterrupt:
        print("stopped")
    pass


def testContinuousServo(kit):
    name = input("Enter Servo name: ")
    min_pulse = json.load(open("ServoCalibration.json", "r"))[f"{name}"]["min_pulse"]
    max_pulse = json.load(open("ServoCalibration.json", "r"))[f"{name}"]["max_pulse"]

    kit.continuous_servo[0].set_pulse_width_range(min_pulse, max_pulse)
    print("Setting power to -0.5")
    kit.continuous_servo[0].throttle = -0.5
    time.sleep(3)

    print("Stopping Servo")
    kit.continuous_servo[0].throttle = 0
    time.sleep(3)

    print("Setting power to 0.5")
    kit.continuous_servo[0].throttle = 0.5
    time.sleep(3)

    print("Stopping Servo")
    kit.continuous_servo[0].throttle = 0
    time.sleep(3)


def testServo(kit):
    range = kit.servo[0].actuation_range
    print("Setting angle to 0º")
    kit.servo[0].angle = 0
    time.sleep(3)

    print("Setting angle to Midpoint")
    kit.servo[0].angle = int(range / 2)
    time.sleep(3)

    print("Setting angle to Max")
    kit.servo[0].angle = int(range)
    time.sleep(3)


if __name__ == "__main__":
    main()
