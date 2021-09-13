import numpy as np


def get_bounds(x):
    return np.min(x, axis=0), np.max(x, axis=0)


def get_patch_nodes(mesh, patch_name):
    # TODO: revisit
    return np.unique(mesh.bnd_patches[patch_name].data)


def rotate(points, angle, rotation_point, axis=2):
    # TODO: validate rotation (try a box -> not well implemented)
    angle = np.deg2rad(angle)
    rotation_point = np.array(rotation_point)
    dim = rotation_point.shape[0]

    rel_points = points - rotation_point
    rot_matrix = define_rotation_matrix(angle, dim=dim, axis=axis)

    return np.matmul(rot_matrix, rel_points.T).T + rotation_point


def define_rotation_matrix(angle, dim=2, axis=2):
    # TODO: rotate around random axis
    if dim == 2:
        return define_rotation_matrix_2d(angle)
    elif dim == 3:
        return define_rotation_matrix_3d(angle, axis=axis)


def define_rotation_matrix_2d(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])


def define_rotation_matrix_3d(angle, axis=2):
    map_ij = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

    rot_matrix = np.zeros((3, 3))
    rot_matrix[axis, axis] = 1
    i, j = map_ij[axis]
    rot_matrix[i, i], rot_matrix[j, j] = np.cos(angle), np.cos(angle)
    rot_matrix[i, j], rot_matrix[j, i] = -np.sin(angle), np.sin(angle)

    return rot_matrix
