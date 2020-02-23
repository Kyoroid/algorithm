from number_theory.prime import modinv


def nCk_mod_v1(n, k, MOD=10**9+7):
    """
    組み合わせの総数C(n, k)を求める
    計算量はO(k)
    """
    r = 1
    kmin = min(k, n-k)
    for i in range(1, kmin+1):
        r = (r * modinv(i, MOD)) % MOD
    for i in range(n-kmin+1, n+1):
        r = r * i % MOD
    return r