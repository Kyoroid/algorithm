from number_theory.prime import *


def modlcm(x, p):
    """
    配列xに対する最小公倍数 LCM(x_1, x_2, ..., x_n) mod p を求める
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
            max_prime_counts[prime] = max(
                max_prime_counts[prime], prime_count[prime])
    # 素因数を結合してLCMを求める
    lcm_value = 1
    for prime, factor in max_prime_counts.items():
        lcm_value *= pow(prime, factor, p)
        lcm_value %= p
    return lcm_value
