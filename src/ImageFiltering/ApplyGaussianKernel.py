import os
from PIL import Image

import Util.PillowUtil as PillowUtil
import Util.KernelUtil as KernelUtil

# Gaussian Kernel
gaussianKernelK1SD1 = KernelUtil.genGaussianKernel(1, sd=1)
gaussianKernelK2SD3 = KernelUtil.genGaussianKernel(2, sd=3)
gaussianKernelK3SD5 = KernelUtil.genGaussianKernel(3, sd=5)

image = Image.open(os.path.dirname(__file__) + "\image.jpg")
image.show(title="Original")

PillowUtil.applyKernel(image, gaussianKernelK1SD1).show(title="GaussianKernel k=1 sd=1")
PillowUtil.applyKernel(image, gaussianKernelK2SD3).show(title="GaussianKernel k=2 sd=3")
PillowUtil.applyKernel(image, gaussianKernelK3SD5).show(title="GaussianKernel k=3 sd=5")

