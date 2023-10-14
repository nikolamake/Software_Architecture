from .Polygon import Polygon
from .Texture import Texture


class PolygonalModel:
    def __init__(self, polygons: list[Polygon], textures=None):  # : [Texture]
        self.polygons = polygons
        self.textures = textures