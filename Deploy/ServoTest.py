import time
from string import printable

from adafruit_servokit import ServoKit


def main():
    kit = ServoKit(channels=16)
    print("This is a test. Will move servo on Channel 0")
    try:
        range = kit.servo[0].actuation_range
        while True:
            print("Setting angle to 0º")
            kit.servo[0].angle = 0
            time.sleep(2)

            print("Setting angle to Midpoint")
            kit.servo[0].angle = int(range / 2)
            time.sleep(2)

            print("Setting angle to Max")
            kit.servo[0].angle = int(range)
            time.sleep(2)

    except KeyboardInterrupt:
        print("stopped")


if __name__ == "__main__":
    main()
