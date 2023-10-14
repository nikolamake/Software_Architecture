from .PolygonalModel import PolygonalModel
from .Flash import Flash



class Scene:
    def __init__(self, id: int, models: list[PolygonalModel], flashes: list[Flash]):
        self.id = id
        self.models = models
        self.flashes = flashes


    def method1(self, type):
        pass

    def method2(self, type1, type2):
        pass
