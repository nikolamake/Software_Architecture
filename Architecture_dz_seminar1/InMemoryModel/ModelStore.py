from Architecture_dz.Architecture_dz_seminar1.ModelElements.PolygonalModel import PolygonalModel
from Architecture_dz.Architecture_dz_seminar1.ModelElements.Scene import Scene
from Architecture_dz.Architecture_dz_seminar1.ModelElements.Flash import Flash
from Architecture_dz.Architecture_dz_seminar1.ModelElements.Camera import Camera
from .IModelChanger import IModelChanger
from .IModelChangedObserver import IModelChangedObserver


class ModelStore:
    def __init__(self, models: list[PolygonalModel], scenes: list[Scene], flashes: list[Flash], cameras: list[Camera], change_observers=None):
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self._change_observers = change_observers

    def get_scene(self, identificator: int):
        pass

    def notify_change(self, obj: IModelChanger):
        pass

