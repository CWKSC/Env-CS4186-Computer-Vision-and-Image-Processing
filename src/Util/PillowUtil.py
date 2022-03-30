from typing import Any, Callable, Generator
from PIL import Image

import Util.Array2DUtil as Array2DUtil


def iter(image: Image) -> Generator:
    return ((x, y) for x in range(image.size[0]) for y in range(image.size[1]))


def iterPixel(image: Image) -> Generator:
    pixels = image.load()
    return ((pixels[x, y], x, y) for (x, y) in iter(image))


def mapPixel(
    image: Image,
    mapPixel: Callable[
        [(int | tuple[int, int, int]), int, int], (int | tuple[int, int, int])
    ],
) -> Image:
    pixels = image.load()
    for (r, c) in iter(image):
        pixels[r, c] = mapPixel(pixels[r, c], r, c)
    return image


def getPixelArray2D(image: Image) -> list:
    pixels = image.load()
    return [[pixels[x, y] for y in range(image.size[1])] for x in range(image.size[0])]


def array2DToImage(array2d: list[list[Any]], mode: str) -> Image:
    (row, col) = Array2DUtil.getRowCol(array2d)
    result = Image.new(mode, (row, col))
    mapPixel(result, lambda pixel, r, c: array2d[r][c])
    return result
