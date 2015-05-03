from math import atan2, pi
from Section import Section

class RingAbstractSection(Section):
    def __init__(self, name, colour, startAngle, angle):
        Section.__init__(self, name, colour)
        self.angle = angle
        self.startAngle = startAngle
        self.endAngle = (startAngle+angle)
        self.centerX = 11989.075
        self.centerY = 4827.0225
        self.radius = 2705.4143

    def isInUpperHalf(self):
        numbersOfAngle = [x for x in range(int(self.startAngle), int(self.endAngle))]
        numbersOfUpperHalf = [x for x in range(-90, 90)]
        listsIntersection = set(numbersOfAngle).intersection(numbersOfUpperHalf)
        percentInUpperHalf = len(listsIntersection) / float(len(numbersOfAngle))
        if percentInUpperHalf > 0.5:
            return True
        else:
            return False

    def getAngleBetweenDevices(self):
        return self.angle/float(self.numberOfDevices()+1)

    def sortDevices(self):
        self.devices = sorted(self.devices, cmp=self.compare)
        self.assignNumbersInSection()

    def compare(self, dev1, dev2):
        a = list(dev1.realCoordinates)
        b = list(dev2.realCoordinates)

        a[0] += self.centerX
        b[0] += self.centerX
        a[1] += self.centerY
        b[1] += self.centerY

        phiA = atan2(a[1], a[0])
        phiB = atan2(b[1], b[0])

        degA = phiA * (180.0/pi) + self.startAngle - 91
        degB = phiB * (180.0/pi) + self.startAngle - 91

        if degA < 0:
            degA += 360.0
        if degB < 0:
            degB += 360.0

        if degA < degB:
            return 1
        elif degA > degB:
            return -1
        else:
            return 0