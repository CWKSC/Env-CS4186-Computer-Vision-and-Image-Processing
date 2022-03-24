import numpy as np


def getCoOccurrenceMatrix(image, d):
    """
    Calculates the co-occurrence matrix of an image.
    @param image: the image to calculate the co-occurrence matrix for
    @param d: the distance to consider
    @return: the co-occurrence matrix
    """
    dr = d[0]
    dc = d[1]
    # get the image dimensions
    rows = len(image)
    cols = len(image[0])
    # create the co-occurrence matrix
    coOccurrenceMatrix = {}
    for row in range(rows - dr):
        for col in range(cols - dc):
            pixel = image[row][col]
            offsetPixel = image[row + dr][col + dc]
            if (pixel, offsetPixel) not in coOccurrenceMatrix:
                coOccurrenceMatrix[(pixel, offsetPixel)] = 1
            else:
                coOccurrenceMatrix[(pixel, offsetPixel)] += 1
    return coOccurrenceMatrix


print(
    getCoOccurrenceMatrix(
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 2, 2],
            [0, 0, 2, 2],
            [0, 0, 2, 2],
            [0, 0, 2, 2],
        ],
        (3, 1),
    )
)
