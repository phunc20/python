## 2022/11/08
As of this date, only three Japanese models are of interest on Hugging Face:
1. `sonoisa/sentence-bert-base-ja-mean-tokens`
2. `sonoisa/sentence-bert-base-ja-mean-tokens-v2`
3. `colorfulscoop/sbert-base-ja`

In addition to `sentence-transformers`, one needs to
```sh
pip install -r requirements.txt
```

as indicated in <https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2>

> 事前学習済みモデルとしてcl-tohoku/bert-base-japanese-whole-word-maskingを利用しました。
> 従って、推論の実行にはfugashiとipadicが必要です（pip install fugashi ipadic）。

Moreover, the model weights need to be downloaded. One could make use of the script `install.py`
to install and test by running
```sh
python install.py
```






