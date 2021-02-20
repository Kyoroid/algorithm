from lib.integer.extgcd import extgcd


class InversionError(Exception):
    def __init__(self):
        self.message = "Inverse element is not defined."


def mod_inv(a: int, n: int) -> int:
    """逆元を求める。

    Parameters
    ----------
    a : int
        逆元を求めたい整数
    n : int
        法

    Returns
    -------
    int
        逆元

    Raises
    ------
    ArithmeticError
        逆元が存在しない場合に送出する
    """
    d, x, y = extgcd(a, n)
    if d != 1:
        raise InversionError()
    return x % n


def mod_pow(a: int, x: int, p: int) -> int:
    """素数の法 p のもとで、繰り返し二乗法により冪乗を求める。負の指数にも対応する。

    Parameters
    ----------
    a : int
        底
    x : int
        指数
    p : int
        法

    Returns
    -------
    int
        冪乗
    """
    x %= p - 1
    y = 1
    while x > 0:
        if x & 1 == 1:
            y *= a
            y %= p
        x >>= 1
        a *= a
        a %= p
    return y
