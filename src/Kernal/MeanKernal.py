# Mean Kernal is all element with 1 / total number of element

import numpy as np

def genMeanKernal(k = 1):
    length = 2 * k + 1
    return np.full((length, length), 1 / (length * length))

print(genMeanKernal(1))
# [[0.11111111 0.11111111 0.11111111]
#  [0.11111111 0.11111111 0.11111111]
#  [0.11111111 0.11111111 0.11111111]]

print(genMeanKernal(2))
# [[0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]]