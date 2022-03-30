from multiprocessing.dummy import Array
import os
from PIL import Image

import Util.PillowUtil as PillowUtil
import Util.KernalUtil as KernalUtil
import Util.Array2DUtil as Array2DUtil

image = Image.open(os.path.dirname(__file__) + "\image.jpg")
grayImage = image.convert("L")
grayPixels = PillowUtil.getPixelArray2D(grayImage)

gaussianKernelK1SD1 = KernalUtil.genGaussianKernel(1, sd=1)
gaussianKernelK3SD5 = KernalUtil.genGaussianKernel(3, sd=5)

filteredPixels = KernalUtil.applyKernal(grayPixels, gaussianKernelK1SD1)
filteredIntPixels = Array2DUtil.map(filteredPixels, lambda ele, r, c: int(ele))
filteredImage = PillowUtil.array2DToImage(filteredIntPixels, "L")
filteredImage.show()

filteredPixels = KernalUtil.applyKernal(grayPixels, gaussianKernelK3SD5)
filteredIntPixels = Array2DUtil.map(filteredPixels, lambda ele, r, c: int(ele))
filteredImage = PillowUtil.array2DToImage(filteredIntPixels, "L")
filteredImage.show()

