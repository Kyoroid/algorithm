import numpy as np
from numba import jitclass, i8


@jitclass([("n", i8), ("tree", i8[:])])
class FenwickTree:
    def __init__(self, n: i8) -> None:
        """Fenwick Treeを初期化します。

        Parameters
        ----------
        n : i8
            要素数
        """
        self.n = n
        self.tree = np.zeros(n + 1, dtype=np.int64)
    
    def _rsum(self, r):
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r
        return s

    def sum(self, l: i8, r: i8) -> i8:
        """区間[l, r) の総和を返します。

        Parameters
        ----------
        l : i8
            区間の左端
        r : i8
            区間の右端

        Returns
        -------
        i8
            区間[l, r) の総和
        """
        return self._rsum(r) - self._rsum(l)

    def add(self, i: i8, x: i8) -> None:
        """添字iにxを加算します。

        Parameters
        ----------
        i : i8
            添字
        x : i8
            加数
        """
        i += 1
        while i <= self.n:
            self.tree[i] += x
            i += i & -i
