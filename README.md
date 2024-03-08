# Dependency

easy-diff depends on `koui`.

please install `koui` as below.

`pip install koui`


# How to use

execute `easy-diff.py` as below.

`python easy-diff.py`

if you want to compare `soseki.txt` as `I am a cat` with `ogai.txt` as `Maihime`, enter like as below.

```
please enter the first text name. I am a cat
please enter the first input file path. cat.txt

please enter the first text name. Maihime
please enter the first input file path. ogai.txt
```

you get diff as`out.xml` and `out.html`, also Levenshtein distance as `distance.csv`.


# Rights

part of easy-diff is originally written by Satoru Nakamura.

[二つのテキスト間の差分を抽出するプログラムを作成しました。](https://zenn.dev/nakamura196/articles/442da1c74afae1)

[校異情報の生成.ipynb](https://colab.research.google.com/github/nakamura196/ndl_ocr/blob/main/%E6%A0%A1%E7%95%B0%E6%83%85%E5%A0%B1%E3%81%AE%E7%94%9F%E6%88%90.ipynb)

easy-diff is editted for local environment by Shiyuu Shimomura.