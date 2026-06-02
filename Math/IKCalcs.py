import matplotlib.pyplot as plt
import numpy as np

from Math.Segment import Segment

arm: list[Segment] = []


def main():
    seg1 = Segment(1.0, 45)
    seg2 = Segment(1.0, -20)
    arm.extend([seg1, seg2])
    drawCurrentPose()
    pass


def drawCurrentPose():
    x = [0.0]
    y = [0.0]
    for i in range(len(arm)):
        x.append(x[i] + arm[i].getRelativeXCoordinate())
        y.append(y[i] + arm[i].getRelativeYCoordinate())

    plt.plot(x, y, "-o")
    plt.axis("equal")
    plt.grid(True)
    plt.show()
    pass


if __name__ == "__main__":
    main()
