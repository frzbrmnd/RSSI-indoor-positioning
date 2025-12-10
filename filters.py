import numpy as np

class KalmanFilter2D:
    def __init__(self):
        self.x = np.zeros((4, 1))  # [x, y, vx, vy]
        self.P = np.eye(4) * 500
        self.F = np.eye(4)
        self.H = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0]])
        self.R = np.eye(2) * 2
        self.Q = np.eye(4) * 0.1

    def predict(self, dt=1.0):
        self.F[0,2] = dt
        self.F[1,3] = dt
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        z = np.array(z).reshape(2,1)
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(4) - K @ self.H) @ self.P
        return self.x
