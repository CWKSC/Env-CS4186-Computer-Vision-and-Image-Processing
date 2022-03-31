# Mean Kernel is all element with 1 / total number of element

import Util.KernelUtil as KernelUtil

print(KernelUtil.genMeanKernel(1))
# [[0.11111111 0.11111111 0.11111111]
#  [0.11111111 0.11111111 0.11111111]
#  [0.11111111 0.11111111 0.11111111]]

print(KernelUtil.genMeanKernel(2))
# [[0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]
#  [0.04 0.04 0.04 0.04 0.04]]