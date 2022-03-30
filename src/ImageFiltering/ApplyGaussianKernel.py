import os
from PIL import Image

import Util.PillowUtil as PillowUtil
import Util.KernalUtil as KernalUtil

image = Image.open(os.path.dirname(__file__) + '\image.jpg')
grayImage = image.convert('L')

grayPixels = PillowUtil.getPixelArray2D(grayImage)
filteredPixels = KernalUtil.applyKernal(grayPixels, KernalUtil.genGaussianKernel(1))

filteredImage = PillowUtil.array2DToImage(filteredPixels, 'L')
filteredImage.show()


