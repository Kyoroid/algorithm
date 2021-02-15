from __future__ import annotations


def mod_comb(n: int, k: int, p: int, f: list[int], invf: list[int]) -> int:
    """法 p のもとで、組み合わせの場合の数を求める。

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
        組み合わせの場合の数
    """
    c = f[n]
    c = c * invf[n-k] % p
    c = c * invf[k] % p
    return c
