import Util.Array2DUtil as Array2DUtil


def test_center2dIter():
    assert list(Array2DUtil.centerAlignIter([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (0, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
