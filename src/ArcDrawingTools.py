from math import pi, cos, sin

class ArcDrawingTools:
    def __init__(self):
        pass

    @staticmethod
    def describeArcClockwise( x, y, radius,startAngle, endAngle):
        d = ArcDrawingTools.describePathForTextClockwise(x, y, radius, startAngle, endAngle)
        start = ArcDrawingTools.polarToCartesian(x, y, radius, endAngle)
        path = ["L", x, y, "L", start[0], start[1], "Z"]
        d += " ".join([str(x) for x in path])
        return d

    @staticmethod
    def describeArcAnticlockwise(x, y, radius,startAngle, endAngle):
        d = ArcDrawingTools.describePathForTextAnticlockwise(x, y, radius, startAngle, endAngle)
        end = ArcDrawingTools.polarToCartesian(x, y, radius, startAngle)
        path = ["L", x, y, "L", end[0], end[1], "Z"]
        d += " ".join([str(x) for x in path])
        return d

    @staticmethod
    def describePathForTextClockwise( x, y, radius,startAngle, endAngle):
        start, end, arcSweep = ArcDrawingTools.describeArcHelper(x, y, radius, startAngle, endAngle)
        d = ["M", start[0], start[1], "A", radius, radius, 0, arcSweep, 0, end[0], end[1]]
        return " ".join([str(x) for x in d])

    @staticmethod
    def describePathForTextAnticlockwise( x, y, radius,startAngle, endAngle):
        start, end, arcSweep = ArcDrawingTools.describeArcHelper(x, y, radius, startAngle, endAngle)
        d = ["M", end[0], end[1], "A", radius, radius, 0, arcSweep, 1, start[0], start[1]]
        return " ".join([str(x) for x in d])

    @staticmethod
    def describeArcHelper(x, y, radius, startAngle, endAngle):
        start = ArcDrawingTools.polarToCartesian(x, y, radius, endAngle)
        end = ArcDrawingTools.polarToCartesian(x, y, radius, startAngle)
        arcSweep = "0" if endAngle - startAngle <= 180 else "1"
        return [start, end, arcSweep]

    @staticmethod
    def polarToCartesian(centerX, centerY, radius, angleInDegrees):
        angleInRadians = (angleInDegrees-90.0) * pi / 180.0
        x = centerX + (radius * cos(angleInRadians))
        y = centerY + (radius * sin(angleInRadians))
        return [x, y]