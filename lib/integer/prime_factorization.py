from __future__ import annotations
import math


def prime_factorization(n: int) -> tuple[list[int], list[int]]:
    """素因数分解を行う。

    Parameters
    ----------
    n : int
        素因数分解の対象となる自然数

    Returns
    -------
    tuple[list[int], list[int]]
        (素因数リスト, 個数リスト) のタプル
    """
    if n == 1:
        return ([1], [1])
    factors = []
    counts = []
    for i in range(2, math.isqrt(n)+1):
        if i * i > n:
            break
        if n % i == 0:
            factors.append(i)
            n //= i
            count = 1
            while n % i == 0:
                n //= i
                count += 1
            counts.append(count)
    if n > 1:
        factors.append(n)
        counts.append(1)
    return factors, counts


def list_spf(n: int) -> list[int]:
    """素因数分解の前処理として、最小の素因数を列挙する。

    Parameters
    ----------
    n : int
        素因数分解を求める数の上限 (自身を含む)

    Returns
    -------
    list[int]
        最小の素因数のリスト
    """
    spf = [1] * (n+1)
    spf[0] = 0
    spf[1] = 1
    for a in range(2, n+1):
        if spf[a] == 1:
            spf[a] = a
            for i in range(a*a, n+1, a):
                if spf[i] == 1:
                    spf[i] = a
    return spf


def prime_factorization_spf(n: int, spf: list[int]) -> tuple[list[int], list[int]]:
    """最小の素因数のリストを用いて、素因数分解を行う。

    Parameters
    ----------
    n : int
        素因数分解の対象となる自然数
    spf : list[int]
        最小の素因数のリスト

    Returns
    -------
    tuple[list[int], list[int]]
        (素因数リスト, 個数リスト) のタプル
    """
    if n == 1:
        return ([1], [1])
    factors = []
    counts = []
    while n > 1:
        factor = spf[n]
        count = 1
        n //= factor
        while factor == spf[n]:
            count += 1
            n //= factor
        factors.append(factor)
        counts.append(count)
    return factors, counts
