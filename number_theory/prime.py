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


def prime_factorization(it):
    """
    数値の素因数分解をリストで返すイテレータ
    エラトステネスの篩を応用する 計算量O(A+Nlog(log(N)))
    """
    n = max(it)
    factor = [1 for i in range(n+1)]
    factor[0] = 0
    factor[1] = 1
    for i in range(2, n+1):
        if factor[i] == 1:
            for j in range(i, n+1, i):
                factor[j] = i
    for a in it:
        if a < 1:
            raise ValueError('Number must be larger than 0')
        if a == 1:
            yield list()
        else:
            prime_factors = list()
            while a != factor[a]:
                prime_factors.append(factor[a])
                a //= factor[a]
            prime_factors.append(factor[a])
            yield list(sorted(prime_factors))
