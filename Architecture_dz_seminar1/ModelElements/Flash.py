from .Polygon import Point3D

class Angle3D:
    def __init__(self, list):
        self.list = list

class Flash:
    def __init__(self, location: Point3D, angle: 'Angle3D', colour: 'Colour', power: float):
        self.location = location
        self.angle = angle
        self.colour = colour
        self.power = power

    def rotate(self, angle: 'Angle3D'):
        pass

    def move(self, point: 'Point3D'):
        pass