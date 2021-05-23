from __future__ import annotations


def euler_tour(n: int, g: list[list[int]]) -> tuple[list[int], list[int], list[int]]:
    """木に対しオイラーツアーを実行します。

    Parameters
    ----------
    n : int
        木のノード数
    g : list[list[int]]
        木を表す隣接リスト

    Returns
    -------
    tuple[list[int], list[int], list[int]]
        (入時刻、出時刻、深さ) のタプル
    """


    t_in = [0] * n
    t_out = [0] * n
    depth = [-1] * n
        
    def dfs(u, t=0):
        t_in[u] = t
        t += 1
        for v in g[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                t = dfs(v, t)
        t_out[u] = t
        t += 1
        return t
    
    depth[0] = 0
    dfs(0)
    return t_in, t_out, depth
