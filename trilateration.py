import numpy as np

# Convert RSSI to distance (meters)
def rssi_to_distance(rssi, A=-40, n=2.0):
    """Convert RSSI to approximate distance in meters."""
    return 10 ** ((A - rssi) / (10 * n))

# calculate location
def trilaterate(routers, distances):
    """
    routers: list of (x, y)
    distances: list of distance estimates
    """
    P1, P2, P3 = map(np.array, routers)
    r1, r2, r3 = distances

    ex = (P2 - P1) / np.linalg.norm(P2 - P1)
    i = np.dot(ex, P3 - P1)
    ey = (P3 - P1 - i * ex) / np.linalg.norm(P3 - P1 - i * ex)
    d = np.linalg.norm(P2 - P1)
    j = np.dot(ey, P3 - P1)

    x = (r1**2 - r2**2 + d**2) / (2 * d)
    y = (r1**2 - r3**2 + i**2 + j**2) / (2 * j) - (i / j) * x

    pos = P1 + x * ex + y * ey
    return pos