import json
import time

from adafruit_servokit import ServoKit


def main():
    print("This is a test.")

    if (input("Is this a continuous servo? (t or f)")) == "t":
        continuous_servo = True
    else:
        continuous_servo = False

    slot = input("Enter slot number: ")

    try:
        kit = ServoKit(channels=16)
        if continuous_servo:
            testContinuousServo(kit, slot)
        else:
            testServo(kit, slot)

    except KeyboardInterrupt:
        print("stopped")
    pass


def testContinuousServo(kit, slot):
    name = input("Enter Servo name: ")
    min_pulse = json.load(open("ServoCalibration.json", "r"))[f"{name}"]["min_pulse"]
    max_pulse = json.load(open("ServoCalibration.json", "r"))[f"{name}"]["max_pulse"]

    kit.continuous_servo[slot].set_pulse_width_range(min_pulse, max_pulse)
    print("Setting power to -0.5")
    kit.continuous_servo[slot].throttle = -0.5
    time.sleep(3)

    print("Stopping Servo")
    kit.continuous_servo[slot].throttle = 0
    time.sleep(3)

    print("Setting power to 0.5")
    kit.continuous_servo[slot].throttle = 0.5
    time.sleep(3)

    print("Stopping Servo")
    kit.continuous_servo[slot].throttle = 0
    time.sleep(3)


def testServo(kit, slot):
    range = kit.servo[slot].actuation_range
    print("Setting angle to 0º")
    kit.servo[slot].angle = 0
    time.sleep(3)

    print("Setting angle to Midpoint")
    kit.servo[slot].angle = int(range / 2)
    time.sleep(3)

    print("Setting angle to Max")
    kit.servo[slot].angle = int(range)
    time.sleep(3)


if __name__ == "__main__":
    main()
