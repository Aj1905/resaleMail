# 環境構築

Mac 環境構築 

---

## 1. ターミナルの起動

Mac のターミナルを起動します。

---

## 2. プロジェクトディレクトリへの移動

作業中のプロジェクトディレクトリに移動してください

## 3. 仮想環境の作成

Python の内蔵モジュール `venv` を使って仮想環境を作成します。以下のコマンドでは仮想環境のディレクトリ名を `venv` にしています。
```bash
python3 -m venv venv
```

## 4. 仮想環境のアクティベート

作成した仮想環境をアクティベートします。
```bash
source venv/bin/activate
```

## 5. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```


# 買取一丁目

## 概要

- 各ジャンルにURLが用意されている。
- 一見ページが複数あるように見えるが、実は最初にページにアクセスした時点で全ての商品がDOM上で読み込まれている。なのでページネーションする必要が無い（めっちゃ楽）。
- 商品情報は以下の形式で取得（恐らくジャンルにより異なる）
  ```python
  # スマホ一覧ページ (https://www.1-chome.com/keitai)
  {
      "name": "商品名",
      "type": "キャリアなど", 
      "adjustment": "カラー別調整",
      "new_price": "新品価格",
      "used_price": "中古価格"
  }
  ```