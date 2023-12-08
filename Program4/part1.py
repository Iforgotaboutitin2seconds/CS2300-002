
import numpy as np

def point_plane_distance(point, plane):
    x1, y1, z1 = point
    A, B, C, D = plane
    return abs(A*x1 + B*y1 + C*z1 + D) / np.sqrt(A**2 + B**2 + C**2)

def line_plane_intersection(line_point, line_dir, plane):
    P0 = np.array(line_point)
    v = np.array(line_dir)
    A, B, C, D = plane
    plane_normal = np.array([A, B, C])
    t = -(np.dot(plane_normal, P0) + D) / np.dot(plane_normal, v)
    intersection = P0 + t * v
    return intersection

# Example usage
point = (1, 2, 3)
plane = (4, 5, 6, 7)
print("Distance from point to plane:", point_plane_distance(point, plane))
