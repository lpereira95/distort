import numpy as np

from distort._base import Distorter
from distort.utils import get_patch_nodes
from distort.utils import rotate


class FieldDistorter(Distorter):

    def __init__(self, field):
        self.field = field

    def apply_distortion(self, mesh):
        mesh.points = self.field(mesh.points)


class PatchTranslator(Distorter):

    def __init__(self, patch_name, delta):
        self.delta = delta
        self.patch_name = patch_name

    def apply_distortion(self, mesh):
        patch_nodes = get_patch_nodes(mesh, self.patch_name)
        mesh.points[patch_nodes] += np.array(self.delta)


class PatchRotator(Distorter):

    def __init__(self, patch_name, angle, rotation_point, axis=2):
        self.patch_name = patch_name
        self.angle = angle
        self.rotation_point = rotation_point
        self.axis = axis

    def apply_distortion(self, mesh):
        patch_nodes = get_patch_nodes(mesh, self.patch_name)
        mesh.points[patch_nodes] = rotate(mesh.points[patch_nodes], self.angle,
                                          self.rotation_point, axis=self.axis)


class Attractor(Distorter):

    def __init__(self, attraction_point, radius):
        self.attraction_point = np.array(attraction_point)
        self.radius = radius

    def apply_distortion(self, mesh):
        indices = self.get_neighbor_points_indices(mesh)
        self.collapse_nodes(mesh, indices)

    def get_neighbor_points_indices(self, mesh):
        return np.linalg.norm(mesh.points - self.attraction_point, axis=1) < self.radius

    def collapse_nodes(self, mesh, indices):
        mesh.points[indices] = self.attraction_point
