import numpy as np
def ZSUv():
    # x_shift = 10
    # y_shift = 20
    # return [x_shift, y_shift]
    # return np.array([
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 10],
    #     [0, 0, 0, 10, 20],
    #     [0, 0, 10, 20, 30]
    #     ], dtype=np.float32)
    kernel = np.zeros((20, 20), dtype=np.float32)
    kernel[-1, -1] = 1
    # print(kernel)
    return kernel

def Inversia():
    return np.array([
        [0, 0, 0],
        [0, -1, 0],
        [0, 0, 0]
        ], dtype=np.float32)

def Gauss_11x11():
    return np.array([
        [0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,],
        [0.0000,	0.0000,	0.0000,	0.0000,	0.0001,	0.0001,	0.0001,	0.0000,	0.0000,	0.0000,	0.0000],
        [0.0000,	0.0000,	0.0000,	0.0004,	0.0014,	0.0023,	0.0014,	0.0004,	0.0000,	0.0000,	0.0000,],
        [0.0000,	0.0000,	0.0004,	0.0037,	0.0146,	0.0232,	0.0146,	0.0037,	0.0004,	0.0000,	0.0000,],
        [0.0000,	0.0001,	0.0014,	0.0146,	0.0584,	0.0926,	0.0584,	0.0146,	0.0014,	0.0001,	0.0000,],
        [0.0000,	0.0001,	0.0023,	0.0232,	0.0926,	0.1466,	0.0926,	0.0232,	0.0023,	0.0001,	0.0000,],
        [0.0000,	0.0001,	0.0014,	0.0146,	0.0584,	0.0926,	0.0584,	0.0146,	0.0014,	0.0001,	0.0000,],
        [0.0000,	0.0000,	0.0004,	0.0037,	0.0146,	0.0232,	0.0146,	0.0037,	0.0004,	0.0000,	0.0000,],
        [0.0000,	0.0000,	0.0000,	0.0004,	0.0014,	0.0023,	0.0014,	0.0004,	0.0000,	0.0000,	0.0000,],
        [0.0000,	0.0000,	0.0000,	0.0000,	0.0001,	0.0001,	0.0001,	0.0000,	0.0000,	0.0000,	0.0000,],
        [0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,	0.0000,],
        ], dtype=np.float32)

def Move_diagonal():
    return np.array([
        [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1 ],
        [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0 ],
        [ 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0 ],
        [ 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0 ],
        [ 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0 ],
        [ 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0 ],
        [ 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ],
        ], dtype=np.float32)

def Rizkist():
    return np.array([
        [0, -1, 0,],
        [-1, 5, -1,],
        [0, -1, 0,],
        ], dtype=np.float32)

def Sobel_diag():
    return np.array([
        [-2, -1, 0,],
        [-1, 0, 1,],
        [0, 1, 2,],
        ], dtype=np.float32)

def Border():
    return np.array([
        [-1, -1, -1,],
        [-1, 8, -1,],
        [-1, -1, -1,],
        ], dtype=np.float32)

def My_Kernel():
    return np.array([
        [-21, -1, 11,],
        [-1, 8, -1,],
        [11, -1, -21,],
        ], dtype=np.float32)