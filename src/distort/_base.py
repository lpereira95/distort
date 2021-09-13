
from abc import ABCMeta
from abc import abstractmethod


class Distorter(metaclass=ABCMeta):

    @abstractmethod
    def apply_distortion(self, mesh):
        pass
