def modpow(x, y, z):
    """
    正の整数x, y, zに対して、x^y mod z の値を求める
    前処理なし、クエリO(log(y))
    """
    a = 1
    while y > 0:
        if y & 1 == 1:
            a *= x
            a %= z
        y >>= 1
        x *= x
        x %= z
    return a


def modinv(n, p):
    """
    逆元のmod pを求める
    """
    if n >= p:
        raise ValueError('p must be larger than n')
    return pow(n, p-2, p)
