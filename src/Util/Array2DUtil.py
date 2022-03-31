from typing import Any, Callable, Generator


def zero(row: int, col: int) -> list[list[int]]:
    if row <= 0 or col <= 0:
        raise ValueError("Invalid row or col")
    return [[0 for _ in range(col)] for _ in range(row)]


def paddingZero(row: int, col: int, padding: int) -> list[list[int]]:
    if row <= 0 or col <= 0:
        raise ValueError("Invalid row or col")
    if padding < 0:
        raise ValueError("Invalid padding, padding < 0")
    minRadius = min(row, col) // 2
    if padding > minRadius:
        raise ValueError(
            f"Invalid padding, padding > minRadius, padding: {padding}, minRadius: {minRadius}"
        )
    return zero(row - 2 * padding, col - 2 * padding)


def getRow(array2d: list[list[Any]]) -> int:
    return len(array2d)


def getCol(array2d: list[list[Any]]) -> int:
    return len(array2d[0])


def getRowCol(array2d: list[list[Any]]) -> tuple[int, int]:
    return (getRow(array2d), getCol(array2d))


def getMinRadius(array2d: list[list[Any]]) -> int:
    (row, col) = getRowCol(array2d)
    return min(row, col) // 2


def getRadius(array2d: list[list[Any]]) -> int:
    (row, col) = getRowCol(array2d)
    if row != col:
        raise ValueError(f"row != col, row: {row}, col: {col}")
    return row // 2


def iter(array2d: list[list[Any]]) -> Generator[tuple[int, int], None, None]:
    (row, col) = getRowCol(array2d)
    return ((r, c) for r in range(row) for c in range(col))


def iterEle(array2d: list[list[Any]]) -> Generator[tuple[Any, int, int], None, None]:
    return ((array2d[r][c], r, c) for (r, c) in iter(array2d))


def paddingIter(array2d: list[list[int]], padding: int) -> Generator:
    if padding < 0:
        raise ValueError("Invalid padding, padding < 0")
    minRadius = getMinRadius(array2d)
    if padding > minRadius:
        raise ValueError(
            f"Invalid padding, padding > minRadius, padding: {padding}, minRadius: {minRadius}"
        )
    (row, col) = getRowCol(array2d)
    return (
        (r, c)
        for r in range(padding, row - padding)
        for c in range(padding, col - padding)
    )


def centerAlignOffsetIter(
    array2d: list[list[int]],
) -> Generator[tuple[int, int], None, None]:
    k = getRadius(array2d)
    return ((r - k, c - k) for (r, c) in iter(array2d))


def centerAlignOffsetArray2D(k: int) -> list[list[tuple[int, int]]]:
    return [[(r - k, c - k) for c in range(2 * k + 1)] for r in range(2 * k + 1)]


def map(
    array2d: list[list[Any]], func: Callable[[Any, int, int], Any]
) -> list[list[Any]]:
    (row, col) = getRowCol(array2d)
    return [[func(array2d[r][c], r, c) for c in range(col)] for r in range(row)]


def sum(array2d: list[list[Any]]) -> Any:
    sum: Any = 0
    for (ele, _, _) in iterEle(array2d):
        sum += ele
    return sum
