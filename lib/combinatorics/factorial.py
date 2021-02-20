from __future__ import annotations


def list_mod_facts(n: int, p: int) -> list[int]:
    """0 以上 n 以下の整数に対し、素数の法 p のもとで階乗を計算する。

    Parameters
    ----------
    n : int
        整数の上限 (自身を含む)
    p : int
        素数の法

    Returns
    -------
    list[int]
        階乗リスト
    """
    f = [1 for i in range(n + 1)]
    for i in range(2, n + 1):
        f[i] = f[i - 1] * i % p
    return f


def list_mod_inv_facts(n: int, p: int) -> list[int]:
    """0 以上 n 以下の整数に対し、素数の法 p のもとで階乗を計算する。

    Parameters
    ----------
    n : int
        整数の上限 (自身を含む)
    p : int
        素数の法
    f : list[int]
        素数の法 p のもとでの階乗リスト

    Returns
    -------
    list[int]
        階乗リスト
    """
    invf = [1 for i in range(n + 1)]
    fn = 1
    for i in range(2, n + 1):
        fn = fn * i % p
    invf[n] = pow(fn, p - 2, p)
    for i in range(n, 2, -1):
        invf[i - 1] = invf[i] * i % p
    return invf
