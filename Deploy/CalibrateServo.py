import json
import time

from adafruit_servokit import ServoKit


def calibrateServo(kit: ServoKit):
    name = input("Enter the name of the servo: ")
    slot = input("Enter the slot of the servo: ")
    slot = int(slot)

    # This sweeps through 1480-1550µs in 10µ steps
    for stop_pulse in range(1480, 1560, 10):
        min_pulse = 600
        max_pulse = 2 * stop_pulse - min_pulse
        kit.continuous_servo[slot].set_pulse_width_range(min_pulse, max_pulse)

        kit.continuous_servo[slot].throttle = 0.3
        time.sleep(1)

        kit.continuous_servo[slot].throttle = 0
        time.sleep(2)
        ans = input(
            f"Stop pulse: {stop_pulse} - Did the servo stop? Should I save the value? (y or n):"
        )
        if ans == "y":
            data = {
                f"{name}": {
                    "min_pulse": min_pulse,
                    "stop_pulse": stop_pulse,
                    "max_pulse": max_pulse,
                },
            }

            json.dump(data, open("ServoCalibration.json", "w"))
        break


if __name__ == "__main__":
    kit = ServoKit(channels=16)
    calibrateServo(kit)
