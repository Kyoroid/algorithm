import math
import collections


def prime_sieve(n):
    """
    n以下の素数を昇順に列挙する
    エラトステネスの篩 計算量O(Nlog(log(N)))
    """
    is_prime = [True for i in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i+i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]


def prime_factorization(n):
    """
    数値nの素因数分解をリストで返す
    エラトステネスの篩を応用する 計算量O(Nlog(log(N)))
    """
    if n < 2:
        return list()
    factor = [1 for i in range(n+1)]
    for i in range(2, n+1):
        if factor[i] == 1:
            for j in range(i, n+1, i):
                factor[j] = i
    prime_factors = list()
    while n != factor[n]:
        prime_factors.append(factor[n])
        n //= factor[n]
    prime_factors.append(factor[n])
    return list(sorted(prime_factors))


def lcm(x):
    """
    配列xのLCMを素数の積で表す
    {p_i: n_i}の辞書で返す (p_iはi番目に小さい素数、n_iは出現数)
    """
    max_prime_counts = dict()
    for prime in prime_sieve(max(x)):
        max_prime_counts[prime] = 0
    for a in x:
        prime_count = collections.Counter(prime_factorization(a))
        for prime in prime_count.keys():
            max_prime_counts[prime] = max(max_prime_counts[prime], prime_count[prime])
    return max_prime_counts
