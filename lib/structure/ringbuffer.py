import numpy as np
from numba import njit, i8


def ringbuffer(size: int) -> i8[:]:
    """リングバッファを初期化します。

    Parameters
    ----------
    size : int
        リングバッファに入れる最大の要素数

    Returns
    -------
    i8[:]
        空のリングバッファ
    """
    q = np.zeros((size + 2,), dtype=np.int64)
    q[-2] = 0
    q[-1] = 0
    return q


@njit((i8[:], i8), cache=True)
def rb_append(q: i8[:], v: i8) -> None:
    """リングバッファの末尾に要素を挿入します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ
    v : i8
        挿入する要素
    """
    head, size = q[-2], q[-1]
    qmax = q.size - 2
    tail = (head + size) % qmax
    q[tail] = v
    q[-1] += 1


@njit((i8[:], i8), cache=True)
def rb_appendleft(q: i8[:], v: i8) -> None:
    """リングバッファの先頭に要素を挿入します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ
    v : i8
        挿入する要素
    """
    head, size = q[-2], q[-1]
    qmax = q.size - 2
    head = (head - 1) % qmax
    q[head] = v
    q[-2] = head
    q[-1] += 1


@njit(i8(i8[:]), cache=True)
def rb_pop(q: i8[:]) -> i8:
    """リングバッファの末尾から要素を削除します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ

    Returns
    -------
    v : i8
        削除された末尾の要素
    """
    head, size = q[-2], q[-1]
    qmax = q.size - 2
    tail = (head + size - 1) % qmax
    v = q[tail]
    q[-1] -= 1
    return v


@njit(i8(i8[:]), cache=True)
def rb_popleft(q: i8[:]) -> i8:
    """リングバッファの先頭から要素を削除します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ

    Returns
    -------
    v : i8
        削除された先頭の要素
    """
    head, size = q[-2], q[-1]
    qmax = q.size - 2
    v = q[head]
    head = (head + 1) % qmax
    q[-2] = head
    q[-1] -= 1
    return v


@njit(i8(i8[:]), cache=True)
def rb_peek(q: i8[:]) -> i8:
    """リングバッファの末尾を参照します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ

    Returns
    -------
    v : i8
        末尾の要素
    """
    head, size = q[-2], q[-1]
    qmax = q.size - 2
    tail = (head + size - 1) % qmax
    v = q[tail]
    return v


@njit(i8(i8[:]), cache=True)
def rb_peekleft(q: i8[:]) -> i8:
    """リングバッファの先頭を参照します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ

    Returns
    -------
    v : i8
        先頭の要素
    """
    head, size = q[-2], q[-1]
    v = q[head]
    return v


@njit(i8(i8[:]), cache=True)
def rb_size(q: i8[:]) -> i8:
    """リングバッファの要素数を取得します。

    Parameters
    ----------
    q : i8[:]
        リングバッファ

    Returns
    -------
    c : i8
        要素数
    """
    return q[-1]
