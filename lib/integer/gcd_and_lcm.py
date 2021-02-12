import math


def gcd(a: int, *args: int) -> int:
    """複数の整数に対する最大公約数を求める。

    Parameters
    ----------
    a : int
        最大公約数を求めたい整数の1つ

    Returns
    -------
    int
        最大公約数
    """
    for b in args:
        if a < b:
            a, b = b, a
        while b > 0:
            a, b = b, a % b
    return a


def lcm(a: int, *args: int) -> int:
    """複数の整数に対する最小公倍数を求める。

    Parameters
    ----------
    a : int
        最小公倍数を求めたい整数の1つ

    Returns
    -------
    int
        最小公倍数
    """
    for b in args:
        if b == 0:
            a = 0
        else:
            a = a * b // math.gcd(a, b)
    return a
