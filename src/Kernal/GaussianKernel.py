# Gσ = e^(- (x^2 + y^2) / (2σ^2)) / (2 pi σ^2)
# σ is Standard Deviation (SD)

import numpy as np

def gaussianFunc(x, y, sd=1):
    return np.exp(-(x ** 2 + y ** 2) / (2 * sd ** 2)) / (2 * np.pi * sd ** 2)

def genGaussianKernel(k=1, sd=1):
    x, y = np.mgrid[-k : k + 1, -k : k + 1]
    gaussian_kernel = gaussianFunc(x, y, sd)
    return gaussian_kernel / np.sum(gaussian_kernel)

print(genGaussianKernel(1))
# [[0.07511361 0.1238414  0.07511361]
#  [0.1238414  0.20417996 0.1238414 ]
#  [0.07511361 0.1238414  0.07511361]]

print(genGaussianKernel(2))
# [[0.00296902 0.01330621 0.02193823 0.01330621 0.00296902]
#  [0.01330621 0.0596343  0.09832033 0.0596343  0.01330621]
#  [0.02193823 0.09832033 0.16210282 0.09832033 0.02193823]
#  [0.01330621 0.0596343  0.09832033 0.0596343  0.01330621]
#  [0.00296902 0.01330621 0.02193823 0.01330621 0.00296902]]