from typing import Any, Callable, Generator, Union
import builtins

from PIL import Image
from PIL.Image import Image as ImageType
from py import builtin

import Util.Array2DUtil as Array2DUtil
import Util.KernelUtil as KernelUtil


def iter(image: ImageType) -> Generator[tuple[int, int], None, None]:
    return ((x, y) for x in range(image.size[0]) for y in range(image.size[1]))


def iterPixel(
    image: ImageType,
) -> Generator[tuple[Union[int, tuple[int, int, int]], int, int], None, None]:
    pixels = image.load()
    return ((pixels[x, y], x, y) for (x, y) in iter(image))



def mapPixel(
    image: ImageType,
    mapPixel: Callable[
        [Union[int, tuple[int, int, int]], int, int], Union[int, tuple[int, int, int]]
    ],
) -> ImageType:
    """
    in place
    """
    pixels = image.load()
    for (r, c) in iter(image):
        pixels[r, c] = mapPixel(pixels[r, c], r, c)
    return image

def getPixelArray2D(image: ImageType) -> list[list[Union[int, tuple[int, int, int]]]]:
    pixels = image.load()
    return [[pixels[x, y] for y in range(image.size[1])] for x in range(image.size[0])]

def fromArray2D(array2d: list[list[Any]], mode: str) -> ImageType:
    (row, col) = Array2DUtil.getRowCol(array2d)
    result = Image.new(mode, (row, col))
    mapPixel(result, lambda pixel, r, c: array2d[r][c])
    return result

def applyKernelToOneChannel(image: ImageType, kernel: list[list[int]]) -> ImageType:
    """
    return new image
    """
    pixelsArray2D = getPixelArray2D(image)
    filteredPixels = KernelUtil.applyKernel(pixelsArray2D, kernel)
    filteredIntPixels = Array2DUtil.map(filteredPixels, lambda ele, r, c: int(ele))
    return fromArray2D(filteredIntPixels, image.mode)

def applyKernel(image: ImageType, kernel: list[list[int]]) -> ImageType:
    """
    return new image
    """
    filteredChannelsImages = list(builtins.map(lambda img: applyKernelToOneChannel(img, kernel), image.split()))
    return Image.merge(image.mode, filteredChannelsImages)


