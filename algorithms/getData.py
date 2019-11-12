import numpy as np

def getData():
    matrix = np.array([
        [0,1,0,0,0,0],
        [1,0,1,0,1,0],
        [0,1,0,1,0,0],
        [0,0,1,0,0,1],
        [0,1,0,0,0,1],
        [0,0,0,1,1,0]
    ])
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']

    return matrix, nodes
