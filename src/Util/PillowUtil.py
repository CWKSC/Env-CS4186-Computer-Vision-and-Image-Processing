from typing import Callable, Generator
from PIL import Image


def Iter2D(image: Image) -> Generator:
    return ((x, y) for x in range(image.size[0]) for y in range(image.size[1]))


def ForEachPixels(
    image: Image, returnPixel: Callable[[int, int], tuple[int, int, int]]
) -> Image:
    pixels = image.load()
    for (x, y) in Iter2D(image):
        pixels[x, y] = returnPixel(x, y)
    return image
