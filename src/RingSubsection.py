from RingAbstractSection import RingAbstractSection

class RingSubsection(RingAbstractSection):
    id = 1

    def __init__(self, name, colour, startAngle, angle):
        RingAbstractSection.__init__(self, name, colour, startAngle, angle)
        self.id = RingSubsection.id
        RingSubsection.id += 1
        self.shortName = "ringSubsection" + str(self.id)

    def updateSvg(self):
        pass