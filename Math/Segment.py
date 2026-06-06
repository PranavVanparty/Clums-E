import numpy as np


class Segment:
    len: float
    currentAngle: float
    targetAngle: float

    def __init__(self, len: float, ang: float):
        self.len = len
        self.currentAngle = ang

    def getCurrentAngle(self):
        return self.currentAngle

    def setCurrentAngle(self, ang: float):
        self.currentAngle = ang

    def getTargetAngle(self):
        return self.targetAngle

    def setTargetAngle(self, tarAng: float):
        self.targetAngle = tarAng

    def getErrorFromTarget(self):
        return self.targetAngle - self.currentAngle

    def getRelativeXCoordinate(self) -> float:
        x = self.len * np.cos(np.deg2rad(self.currentAngle))
        return x

    def getRelativeYCoordinate(self) -> float:
        y = self.len * np.sin(np.deg2rad(self.currentAngle))
        return y
