import Util.KernalUtil as KernalUtil

print(KernalUtil.applyKernal(
    [
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
    ],
    KernalUtil.genGaussianKernel(1).tolist(),
))
# [[17.0, 18.000000000000004, 19.0], [22.0, 23.000000000000007, 24.000000000000007], [27.0, 28.0, 29.0]]

