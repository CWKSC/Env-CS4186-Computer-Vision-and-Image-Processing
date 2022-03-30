import pytest
import Util.Array2DUtil as Array2DUtil


def test_zero():

    assert Array2DUtil.zero(1, 1) == [[0]]
    assert Array2DUtil.zero(2, 2) == [[0, 0], [0, 0]]
    assert Array2DUtil.zero(3, 3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert Array2DUtil.zero(4, 4) == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    assert Array2DUtil.zero(2, 5) == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert Array2DUtil.zero(5, 3) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_zero_raise():
    with pytest.raises(ValueError):
        Array2DUtil.zero(-1, -1)
    with pytest.raises(ValueError):
        Array2DUtil.zero(-1, 0)
    with pytest.raises(ValueError):
        Array2DUtil.zero(0, -1)
    with pytest.raises(ValueError):
        Array2DUtil.zero(0, 0)
    with pytest.raises(ValueError):
        Array2DUtil.zero(1, 0)
    with pytest.raises(ValueError):
        Array2DUtil.zero(0, 1)


def test_getRowCol():
    assert Array2DUtil.getRowCol([[1, 2], [3, 4]]) == (2, 2)
    assert Array2DUtil.getRowCol([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == (3, 3)
    assert Array2DUtil.getRowCol([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == (
        3,
        4,
    )
    assert Array2DUtil.getRowCol(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    ) == (3, 5)
    assert Array2DUtil.getRowCol(
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    ) == (5, 3)


def test_getRadius():
    assert Array2DUtil.getRadius([[1]]) == 0
    assert Array2DUtil.getRadius([[1, 2], [3, 4]]) == 1
    assert Array2DUtil.getRadius([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 1
    assert (
        Array2DUtil.getRadius(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
        == 2
    )
    assert (
        Array2DUtil.getRadius(
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ]
        )
        == 2
    )
    assert (
        Array2DUtil.getRadius(
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 36],
            ]
        )
        == 3
    )
    assert (
        Array2DUtil.getRadius(
            [
                [1, 2, 3, 4, 5, 6, 7],
                [8, 9, 10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19, 20, 21],
                [22, 23, 24, 25, 26, 27, 28],
                [29, 30, 31, 32, 33, 34, 35],
                [36, 37, 38, 39, 40, 41, 42],
                [43, 44, 45, 46, 47, 48, 49],
            ]
        )
        == 3
    )


def test_getRadius_raise():
    with pytest.raises(ValueError):
        Array2DUtil.getRadius([[]]) == 0
    with pytest.raises(ValueError):
        Array2DUtil.getRadius([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError):
        Array2DUtil.getRadius([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


def test_getMinRadius():
    assert Array2DUtil.getMinRadius([[1]]) == 0
    assert Array2DUtil.getMinRadius([[1, 2], [3, 4]]) == 1
    assert Array2DUtil.getMinRadius([[1, 2], [3, 4], [5, 6]]) == 1
    assert Array2DUtil.getMinRadius([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 1
    assert (
        Array2DUtil.getMinRadius(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
        == 2
    )
    assert (
        Array2DUtil.getMinRadius(
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
                [17, 18, 19, 20],
            ]
        )
        == 2
    )
    assert (
        Array2DUtil.getMinRadius(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
                [16, 17, 18],
                [19, 20, 21],
            ]
        )
        == 1
    )
    assert (
        Array2DUtil.getMinRadius(
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
                [17, 18, 19, 20],
                [21, 22, 23, 24],
                [25, 26, 27, 28],
            ]
        )
        == 2
    )


def test_iter():
    assert list(Array2DUtil.iter([[1, 2], [3, 4]])) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    ]
    assert list(Array2DUtil.iter([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]
    assert list(
        Array2DUtil.iter(
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
            ]
        )
    ) == [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ]
    assert list(Array2DUtil.iter([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (2, 0),
        (2, 1),
        (3, 0),
        (3, 1),
        (4, 0),
        (4, 1),
    ]


def test_iterEle():
    assert list(Array2DUtil.iterEle([[1, 2], [3, 4]])) == [
        (1, 0, 0),
        (2, 0, 1),
        (3, 1, 0),
        (4, 1, 1),
    ]
    assert list(Array2DUtil.iterEle([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [
        (1, 0, 0),
        (2, 0, 1),
        (3, 0, 2),
        (4, 1, 0),
        (5, 1, 1),
        (6, 1, 2),
        (7, 2, 0),
        (8, 2, 1),
        (9, 2, 2),
    ]
    assert list(Array2DUtil.iterEle([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])) == [
        (1, 0, 0),
        (2, 0, 1),
        (3, 1, 0),
        (4, 1, 1),
        (5, 2, 0),
        (6, 2, 1),
        (7, 3, 0),
        (8, 3, 1),
        (9, 4, 0),
        (10, 4, 1),
    ]


def test_paddingIter():
    assert list(Array2DUtil.paddingIter([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)) == [
        (1, 1)
    ]
    assert list(
        Array2DUtil.paddingIter(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1
        )
    ) == [
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
    ]
    assert (
        list(
            Array2DUtil.paddingIter(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2
            )
        )
        == []
    )
    assert list(
        Array2DUtil.paddingIter(
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
            ],
            2,
        )
    ) == [(2, 2), (2, 3)]


def test_paddingIter_raise():
    with pytest.raises(ValueError):
        list(Array2DUtil.paddingIter([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1))
    with pytest.raises(ValueError):
        list(Array2DUtil.paddingIter([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))


def test_center2dIter():
    assert list(Array2DUtil.centerAlignIter([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
