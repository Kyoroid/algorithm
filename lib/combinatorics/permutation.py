from __future__ import annotations


def mod_perm(n: int, k: int, p: int, f: list[int], invf: list[int]) -> int:
    """法 p のもとで、順列の場合の数を求める。

    Parameters
    ----------
    n : int
        整数の上限 (自身を含む)
    k : int
        選ぶ個数
    p : int
        法
    f : list[int]
        法 p のもとでの階乗リスト
    invf : list[int]
        法 p のもとでの階乗の逆数リスト

    Returns
    -------
    int
        順列の場合の数
    """
    return f[n] * invf[n-k] % p
