from Math.Arm import Arm
from Math.Segment import Segment

arm: list[Segment] = []


def main():
    seg1 = Segment(1.0, 45)
    seg2 = Segment(1.0, -20)
    arm = Arm([seg1, seg2])


if __name__ == "__main__":
    main()
