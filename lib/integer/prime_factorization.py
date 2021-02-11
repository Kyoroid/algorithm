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