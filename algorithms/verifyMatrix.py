import numpy as np

def verifyMatrix(matrix: np.ndarray, nodes: list):
    if matrix.shape[0] == matrix.shape[1]:
        if matrix.shape[0] == len(nodes):
            return True
        else:
            print("!!! ERROR !!!")
            print("> Os nós não são compatíveis com a matrix")
            return False
    else:
        print("!!! ERROR !!!")
        print("> A Matrix não é quadrada")
        return False
