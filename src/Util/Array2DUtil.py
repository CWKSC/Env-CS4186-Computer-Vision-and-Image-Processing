from typing import Any, Generator


def zero(row: int, col: int) -> list[list[Any]]:
    return [[0 for _ in range(col)] for _ in range(row)]


def getRowCol(array2d: list[list[Any]]) -> tuple[int, int]:
    return (len(array2d), len(array2d[0]))


def getRadius(array2d: list[list[int]]) -> int:
    return len(array2d) // 2


def iter(array2d: list[list[int]]) -> Generator:
    (row, col) = getRowCol(array2d)
    return ((x, y) for y in range(row) for x in range(col))


def paddingIter(array2d: list[list[int]], padding: int) -> Generator:
    (row, col) = getRowCol(array2d)
    return (
        (x, y)
        for y in range(padding, row - padding)
        for x in range(padding, col - padding)
    )


def centerAlignIter(array2d: list[list[int]]) -> Generator:
    (row, col) = getRowCol(array2d)
    k = getRadius(array2d)
    return ((x - k, y - k) for y in range(row) for x in range(col))
