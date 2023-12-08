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

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            nums = [float(num) for num in line.split()]
            point = tuple(nums[:3])
            plane = tuple(nums[3:7])
            line_dir = tuple(nums[7:])
            print("Processing point:", point, "and plane:", plane)
            print("Distance from point to plane:", point_plane_distance(point, plane))
            print("Intersection of line (through point with direction", line_dir, ") and plane:", line_plane_intersection(point, line_dir, plane))
            print()

# Example file path
file_path = 'path_to_your_file.txt'
process_file(file_path)
