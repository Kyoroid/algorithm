from __future__ import annotations


def sieve(n: int) -> list[int]:
    """素数を昇順に列挙する。

    Parameters
    ----------
    n : int
        求める素数の上限 (自身を含む)

    Returns
    -------
    list[int]
        素数リスト
    """
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for a in range(2, n+1):
        if is_prime[a]:
            primes.append(a)
            for i in range(a*a, n+1, a):
                is_prime[i] = False
    return primes
