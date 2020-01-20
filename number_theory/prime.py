import collections


def modinv(n, p):
    """
    逆元のmod pを求める
    """
    if n >= p:
        raise ValueError('p must be larger than n')
    return pow(n, p-2, p)


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


def lcm(x, p=-1):
    """
    配列xに対する最小公倍数 LCM(x_1, x_2, ..., x_n) を求める
    p > 0のときはLCM mod pを返す
    """
    max_prime_counts = dict()
    # LCMを素因数の積で表すための準備
    for prime in prime_sieve(max(x)):
        max_prime_counts[prime] = 0
    # 全てのx_iについて素因数分解
    pfs = prime_factorization(x)
    # 素因数を数え上げることにより、LCMを素因数で表現する
    for pf in pfs:
        prime_count = collections.Counter(pf)
        for prime in prime_count.keys():
            max_prime_counts[prime] = max(max_prime_counts[prime], prime_count[prime])
    # 素因数を結合してLCMを求める
    lcm_value = 1
    for prime, factor in max_prime_counts.items():
        if p > 0:
            lcm_value *= pow(prime, factor, p)
            lcm_value %= p
        else:
            lcm_value *= pow(prime, factor)
    return lcm_value