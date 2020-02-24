def nCk_mod_v1(n, k, p=10**9 + 7):
    """
    組み合わせの総数C(n, k)を求める
    C(n, k) = n(n-1)...(n-k+1) / k(k-1)...1
    前処理なし、クエリO(klog(p))
    """
    k = min(k, n-k)
    a = 1
    for i in range(n-k+1, n+1):
        a = a * i % p
    b = 1
    for i in range(1, k+1):
        b = b * i % p
    return a * pow(b, p-2, p) % p


def nCk_mod_v2(it, p=10**9+7):
    """
    整数(n, k)に対して, 組み合わせの総数C(n, k)を求めるイテレータ
    C(n, k) = n! * (k!)^-1 * ((n-k)!)^-1
    前処理O(n)、クエリO(1)
    """
    def _preprocess(n, p):
        f = [0 for i in range(n+1)]  # n!
        invf = [0 for i in range(n+1)]  # (n!)^-1
        f[0] = 1
        f[1] = 1
        invf[0] = 1
        invf[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] * i % p
        invf[n] = pow(f[n], p-2, p)
        for i in range(n, 2, -1):
            invf[i-1] = invf[i] * i % p
        return f, invf

    nmax = max([n for n, k in it])
    f, invf = _preprocess(nmax, p)
    for n, k in it:
        if n < k or n < 0 or k < 0:
            yield 0
        else:
            yield (f[n] * invf[k] % p) * invf[n-k] % p
