class SegmentTree():
    """セグメント木の実装"""

    def __init__(self, size, INF=-100000000):
        """セグメント木の初期化"""
        self.size = size
        self.n = 2 ** ((size-1).bit_length())
        self.treesize = 2 * self.n
        self.inf = INF
        self.tree = [self.inf for i in range(self.treesize)]

    def update(self, key, value):
        """key番目の値をvalueに更新する"""
        k = key + self.n
        self.tree[k] = value
        k >>= 1
        while k > 0:
            self.tree[k] = max(self.tree[k * 2], self.tree[k * 2 + 1])
            k >>= 1

    def query(self, a, b):
        """区間[a, b)の最大値を求める"""
        if a > b:
            raise ValueError("a must be less than equal b.")
        l = self.inf
        r = self.inf
        a += self.n
        b += self.n
        while a < b:
            if a & 1 == 1:
                l = max(l, self.tree[a])
                a += 1
            if b & 1 == 1:
                b -= 1
                r = max(r, self.tree[b])
            a >>= 1
            b >>= 1
        return max(l, r)

    def __setitem__(self, key, value):
        self.update(key, value)

    def __getitem__(self, key):
        left = self.treesize >> 1
        return self.tree[left + key]

    def tolist(self):
        left = self.treesize >> 1
        right = left + self.size
        return self.tree[left:right]

    def __str__(self):
        return str(self.tolist())

    def __repr__(self):
        return str(self)


def seginit(size, init_value=-100000000):
    n = 2 ** ((size-1).bit_length())
    treesize = n * 2
    st = [init_value for i in range(treesize)]
    return st


def segupdate(st, key, value):
    n = len(st) // 2
    k = key + n
    st[k] = value
    k >>= 1
    while k > 0:
        st[k] = max(st[k * 2], st[k * 2 + 1])
        k >>= 1


def segquery(st, a, b, init_value=-100000000):
    if a > b:
        raise ValueError("a must be less than equal b.")
    l = init_value
    r = init_value
    n = len(st) // 2
    a += n
    b += n
    while a < b:
        if a & 1 == 1:
            l = max(l, st[a])
            a += 1
        if b & 1 == 1:
            b -= 1
            r = max(r, st[b])
        a >>= 1
        b >>= 1
    return max(l, r)


def segview(st, size):
    n = len(st) >> 1
    return st[n:n+size]
