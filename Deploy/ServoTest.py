import time

from adafruit_servokit import ServoKit

calibrate = True
continous_servo = True
full_stop_pulse = 0


def main():
    kit = ServoKit(channels=16)
    print("This is a test. Will move servo on Channel 0")
    try:
        if calibrate:
            calibrateServo(kit)
        elif continous_servo:
            testContinousServo(kit)
        else:
            testServo(kit)
        kit.continuous_servo[0].fraction = None

    except KeyboardInterrupt:
        print("stopped")


def calibrateServo(kit: ServoKit):
    # This sweeps through 1480-1550µs in 10µ steps
    for stop_pulse in range(1480, 1560, 10):
        min_pulse = 600
        max_pulse = 2 * stop_pulse - min_pulse
        kit.continuous_servo[0].set_pulse_width_range(min_pulse, max_pulse)

        kit.continuous_servo[0].throttle = 0.3
        time.sleep(1)

        kit.continuous_servo[0].throttle = 0
        time.sleep(2)
        print(f"Stop pulse: {stop_pulse}µs — did the servo stop?")
        if kit.continuous_servo[0].fraction == 0:
            ans = input(
                "The servo seems to have stopped. Should I save the value? (y or n):"
            )
            if ans == "y":
                full_stop_pulse = stop_pulse

    pass


def testContinousServo(kit):
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
