from __future__ import annotations


def list_divisors(n: int, sorted: bool = False) -> list[int]:
    """約数を求める。

    Parameters
    ----------
    n : int
        約数を求めたい整数n
    sorted : bool, optional
        ソート済みの約数リストを返すかどうか、デフォルトは False

    Returns
    -------
    list[int]
        約数リスト
    """
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    if sorted:
        divisors.sort()
    return divisors


def list_multiples(a: int, n: int) -> list[int]:
    """n以下のaの倍数を列挙する。

    Parameters
    ----------
    a : int
        倍数の種類
    n : int
        倍数の上限 (自身を含む)

    Returns
    -------
    list[int]
        倍数リスト
    """
    multiples = []
    for a in range(a, n + 1, a):
        multiples.append(a)
    return multiples


def count_divisors(n: int) -> list[int]:
    """約数の個数をもつテーブルを作成する。

    Parameters
    ----------
    n : int
        約数を求めたい整数の上限 (自身を含む)

    Returns
    -------
    list[int]
        約数の個数をもつテーブル
    """
    counts = [0] * (n + 1)
    a = 1
    while a * a <= n:
        counts[a * a] += 1
        for i in range(a * (a + 1), n + 1, a):
            counts[i] += 2
        a += 1
    return counts
