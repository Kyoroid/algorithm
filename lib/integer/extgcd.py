from __future__ import annotations


def extgcd(a: int, b: int) -> tuple[int, int, int]:
    """ax + by = gcd(a,b) の整数解の1つを求める。

    Parameters
    ----------
    a : int
        xの係数
    b : int
        yの係数

    Returns
    -------
    tuple[int, int, int]
        (gcd(a, b), x, y) のタプル
    """
    if b == 0:
        return (a, 1, 0) if a > 0 else (0, 0, 0)
    p, q = divmod(a, b)
    d, x, y = extgcd(b, q)
    return (d, y, x - p * y)


def solve_linear_equation(a: int, b: int, c: int) -> tuple[bool, int, int]:
    """一次不定方程式 ax + by = c の整数解の1つを求める。

    Parameters
    ----------
    a : int
        xの係数
    b : int
        yの係数
    c : int
        0次項の係数

    Returns
    -------
    tuple[bool, int, int]
        (解の有無, x, y) のタプル、解なしの場合は (False, 0, 0)
    """
    d, x, y = extgcd(a, b)
    p, q = divmod(c, d)
    if q > 0:
        return (False, 0, 0)
    else:
        return (True, x * p, y * p)
