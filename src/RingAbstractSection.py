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