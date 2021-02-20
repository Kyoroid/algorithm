from __future__ import annotations
from collections.abc import Callable, Sequence


class IntervalError(Exception):
    def __init__(self):
        self.message = "Interval [a, b) must be a < b."


class SegmentTree:
    def __init__(
        self, size: int, op: Callable[[int, int], int] = min, init_value: int = 10 ** 8
    ) -> None:
        """セグメント木を初期化する。

        Parameters
        ----------
        size : int
            要素の最大数
        op : Callable[[int, int], int], optional
            累積操作
        init_value : int, optional
            初期値
        """
        self.size = size
        self.op = op
        self.init_value = init_value
        n = 2 ** ((size - 1).bit_length())
        treesize = n * 2
        st = [init_value] * treesize
        self.st = st
        self.offset = len(st) // 2

    @classmethod
    def from_sequence(
        cls,
        a: Sequence[int],
        op: Callable[[int, int], int] = min,
        init_value: int = 10 ** 8,
    ) -> SegmentTree:
        """シーケンスからセグメント木を作成する。

        Parameters
        ----------
        a : Sequence[int]
            シーケンス
        op : Callable[[int, int], int], optional
            累積操作
        init_value : int, optional
            初期値
        """
        st = cls(len(a), op=op, init_value=init_value)
        for i, x in enumerate(a):
            st.set(i, x)
        return st

    def set(self, key: int, value: int) -> None:
        """一点更新を行う。

        Parameters
        ----------
        key : int
            位置
        value : int
            更新後の値
        """
        k = self.offset + key
        self.st[k] = value
        k >>= 1
        while k > 0:
            self.st[k] = self.op(self.st[k * 2], self.st[k * 2 + 1])
            k >>= 1

    def prod(self, a: int, b: int) -> int:
        """区間 [a, b) に対する累積を計算する。

        Parameters
        ----------
        a : int
            区間の下限 (自身を含む)
        b : int
            区間の上限 (自身を含まない)

        Returns
        -------
        int
            累積

        Raises
        ------
        IntervalError
            不正な区間が指定されたとき
        """
        if a >= b:
            raise IntervalError()
        a += self.offset
        b += self.offset - 1
        s = self.init_value
        while a < b:
            if a & 1:
                s = self.op(s, self.st[a])
                a += 1
            a >>= 1
            if not b & 1:
                s = self.op(s, self.st[b])
                b -= 1
            b >>= 1
        if a == b:
            s = self.op(s, self.st[a])
        return s
