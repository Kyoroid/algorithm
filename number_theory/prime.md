# 素数を用いたアルゴリズム

## エラトステネスの篩

[Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)


## 素因数分解

エラトステネスの篩において

sieve[i] := 数値iの最小の素因数

とおくことにより、素因数分解を高速に行うことができる。

|i|1|2|3|4|5|10|20|
|-|-|-|-|-|-|--|--|
|sieve[i]|1|2|3|2|5|2|2|

上記のsieve[i]のテーブルを用いて、数値20の素因数分解を求める。

```
20 / sieve[20] = 20 / 2 = 10
10 / sieve[10] = 10 / 2 = 5
5 / sieve[5] = 5 / 5 = 1
```

この計算結果から素因数分解の形が求まる。

```
20 = sieve[20] * sieve[10] * sieve[5] = 2 * 2 * 5
```

## 数列の最小公倍数 (LCM)

[ABC152-E Flatten youtube解説](https://youtu.be/UTVg7wzMWQc)

LCMは以下の関係が成り立つ。
```
LCM(a, b, c) = LCM(a, LCM(b, c))
```

3つの数程度なら上記の関係式で計算可能だが、数が増えるとLCMが大きくなりすぎて計算時間がかかる。
このような場合は上記の関係式を使わず、素因数の積から組み立てるアプローチをとる。

例えば、数列`[20, 24, 25]`は以下のように素因数分解できる。

```
20 = 2^2 + 5^1
24 = 2^3 + 3^1
25 = 5^2
```

LCMを求めるには、素因数それぞれについて出現回数の最大値を取り出す。

|prime|2|3|5|7|11|13|17|19|
|-----|-|-|-|-|--|--|--|--|
|   20|2|0|1|0| 0| 0| 0| 0|
|   24|**3**|**1**|0|0| 0| 0| 0| 0|
|   25|0|0|**2**|0| 0| 0| 0| 0|
|LCM(20, 24, 25)|3|1|2|0|0| 0| 0| 0|

上記の表より、LCM(20, 24, 25) を素因数分解した形が求まる。
```
LCM(20, 24, 25) = 2^3 * 3^1 * 5^2 = 600
```
pythonでLCM (mod p)の値を求めるには、べき乗の部分を`pow(x,y,p)`で計算しつつ掛け合わせればよい。