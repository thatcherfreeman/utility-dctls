import numpy as np
from scipy.optimize import minimize


def solve_ax0(A: np.ndarray) -> np.ndarray:
    """Find x = [a, b, 1-a-b] minimizing ||Ax||^2."""
    assert A.shape == (3, 3)

    def objective(params):
        a, b = params
        x = np.array([[a, b, 1.0 - a - b]]).T
        residual = A @ x
        return float(residual.T @ residual)

    result = minimize(objective, x0=[0.2, 0.7], method="Nelder-Mead")
    a, b = result.x
    x = np.array([[a, b, 1.0 - a - b]]).T
    return x


def make_rotation_matrix_axis(axis: np.ndarray, angle_rad: float) -> np.ndarray:
    # Axis assumed to be unit vector, angle assumed to be in radians
    c = np.cos(angle_rad)
    s = np.sin(angle_rad)

    mat = np.zeros((3, 3))
    mat[0][0] = c + axis[0]**2 * (1.0 - c)
    mat[0][1] = axis[0] * axis[1] * (1.0 - c) - axis[2] * s
    mat[0][2] = axis[0] * axis[2] * (1.0 - c) + axis[1] * s
    mat[1][0] = axis[0] * axis[1] * (1.0 - c) + axis[2] * s
    mat[1][1] = c + axis[1]**2 * (1.0 - c)
    mat[1][2] = axis[1] * axis[2] * (1.0 - c) - axis[0] * s
    mat[2][0] = axis[2] * axis[0] * (1.0 - c) - axis[1] * s
    mat[2][1] = axis[2] * axis[1] * (1.0 - c) + axis[0] * s
    mat[2][2] = c + axis[2]**2 * (1.0 - c)
    return mat


def build_matrix(param1, param2):
    # Example of building a matrix from parameters, this can be customized as needed
    return np.array([
        [0.21, 0.7, 0.09],
        [1.0, -1 * (1.0 - param2), -1 * param2],
        [0.0, -param1, param1],
    ])

def solve_rotation_matrices(A: np.ndarray, angle_rad: float) -> np.ndarray:
    """Find B such that A = inv(B) @ R @ B, where R is a 2d rotation matrix by angle_rad.
    """
    assert A.shape == (3, 3)
    R = np.array([
        [1, 0, 0],
        [0, np.cos(angle_rad), -np.sin(angle_rad)],
        [0, np.sin(angle_rad), np.cos(angle_rad)],
    ])

    def objective(params):
        B = build_matrix(params[0], params[1])
        B_inv = np.linalg.pinv(B)
        fit = np.linalg.norm(A - B_inv @ R @ B)
        return fit

    initial_params = [1.0695, 0.4]
    result = minimize(objective, x0=initial_params, method="Nelder-Mead")

    B = build_matrix(result.x[0], result.x[1])
    return B, R

def main():
    A = np.array([
        [0.0,  -.02  , 1.02    ],
        [ 0.372169,  0.827449,  -.199618  ],
        [ -.5613325,  1.3887757, .17255666 ],
    ]).T - np.eye(3)

    x = solve_ax0(A)
    print("Recovered x:", x)
    print("A @ x =", A @ x)
    print("||Ax||^2 =", np.sum((A @ x) ** 2))


    # Measured matrix from setting hue slider to 25 (-90 egrees).
    A = np.array([
        [0.0,  -.02  , 1.02    ],
        [ 0.372169,  0.827449,  -.199618  ],
        [ -.5613325,  1.3887757, .17255666 ],
    ])

    # Loose fit via other regression notebook.
    B_temp = np.array([
        # [0.2126, 0.7152, 0.0722],
        [0.21, 0.7, 0.09],
        [1.0, -0.6, -0.4],
        [0.0, -1.0695, 1.0695],
    ])

    print("b temp", B_temp)
    print("build matrix: ", build_matrix(1.0695, 0.4))

    # R = make_rotation_matrix_axis(lum_coeffs / np.linalg.norm(lum_coeffs), np.radians(-90))
    angle = -90
    R = np.array([
        [1, 0, 0],
        [0, np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
        [0, np.sin(np.radians(angle)), np.cos(np.radians(angle))],
    ])

    # Test case, this should be in similar ballpark.
    print("A reconstruction: ", np.linalg.inv(B_temp) @ R @ B_temp)
    print("A Original      : ", A)
    print(np.linalg.norm(A - np.linalg.inv(B_temp) @ R @ B_temp))

    # Solve the last two rows of B_temp
    B, R = solve_rotation_matrices(A, angle_rad=np.radians(angle))
    print("Recovered B:", B)
    print("Recovered R:", R)
    print("Check A ≈ inv(B) @ R @ B:", A - np.linalg.pinv(B) @ R @ B)
    print(np.mean((A - np.linalg.pinv(B) @ R @ B)**2))


if __name__ == "__main__":
    main()
