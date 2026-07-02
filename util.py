import numpy as np

def get_angle(a, b, c):
    """Calculates the angle at joint b given three 2D points a, b, and c."""
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radians))
    if angle > 180.0:
        angle = 360.0 - angle
    return angle


def get_distance(landmark_list):
    """Calculates the Euclidean distance between two 2D points."""
    if len(landmark_list) < 2:
        return 0
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    return np.hypot(x2 - x1, y2 - y1)
