# 環境構築

## 前提

- Python3.8をインストール済み

## 1. Pandocのインストール

次のリンク先からPandocのインストーラを入手し、インストールを実施する
[https://pandoc.org/installing.html](https://pandoc.org/installing.html)

## 2. 仮想環境の作成

まず、Python3.8の仮想環境を作る。

```shell
$ python -V
Python 3.8.5
$ python -m venv py38env
```

仮想環境を有効化した後、依存するモジュールをインストールする。

```shell
(py38env) $ pip install -r requirements/atcoder_py38_requirements.txt
(py38env) $ pip install -r requirements/notebook_requirements.txt
```

## 3. Jupyter kernel の作成

仮想環境からkernelを作成する。

```shell
(py38env) $ python -m ipykernel install --name py38env
(py38env) $ jupyter kernelspec list
```

## 4. 動作確認

Windowsの場合は`make`を`./make`に読み替える。

```shell
(py38env) $ make html
(py38env) $ make htmlview
```
