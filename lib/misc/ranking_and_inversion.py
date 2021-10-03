import numpy as np
from numba import njit, i8
from lib.structure.fenwick_tree import FenwickTree


@njit("i8[:](i8[:])", cache=True)
def rank_vector(a: i8[:]) -> i8[:]:
    """配列の各要素の順位を求めます。同じ値をもつ要素同士は、もとの順序を保ったまま順位づけされます。

    Parameters
    ----------
    a : i8[:]
        配列

    Returns
    -------
    i8[:]
        配列の各要素の順位
    """
    order = np.argsort(a, kind="mergesort")
    rank = np.argsort(order, kind="mergesort")
    return rank



@njit("i8[:](i8[:])", cache=True)
def inversion_vector(a: i8[:]) -> i8[:]:
    """配列の転倒ベクトル V[i] = #{(A[i], A[k]) | i < k and A[i] >= A[k]} を求めます。

    Parameters
    ----------
    a : i8[:]
        配列

    Returns
    -------
    i8[:]
        転倒ベクトル
    """
    rank = rank_vector(a)
    ft = FenwickTree(a.size)
    inv_vec = np.zeros_like(a)
    for i in range(ft.n - 1, -1, -1):
        ri = rank[i]
        inv_vec[i] = ft.sum(0, ri)
        ft.add(ri, 1)
    return inv_vec
