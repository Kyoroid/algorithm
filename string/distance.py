def levenshtein(str1, str2):
    """
    Levenshtein距離を求める
    """
    m = len(str1)
    n = len(str2)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(m):
        for j in range(n):
            cost = 0 if str1[i] == str2[j] else 1
            dp[i+1][j+1] = min(dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j]+cost)
    return dp[-1][-1]

    