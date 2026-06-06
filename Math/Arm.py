import matplotlib.pyplot as plt

from Math.Segment import Segment


class Arm:
    def __init__(self, segments: list[Segment]):
        self.segments = segments

    def updateSegments(self, segments: list[Segment]):
        self.segments = segments

    def drawCurrentPose(self):
        x = [0.0]
        y = [0.0]
        for i in range(len(self.segments)):
            x.append(x[i] + self.segments[i].getRelativeXCoordinate())
            y.append(y[i] + self.segments[i].getRelativeYCoordinate())

        plt.plot(x, y, "-o")
        plt.axis("equal")

        plt.grid(True)
        plt.show()
        pass
