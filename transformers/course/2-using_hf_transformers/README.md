



## Cache
When we call a checkpoint by specifying its name and when that name exists in the HF-hub, `transformers` package
will download the model's configuration file and weight file for us. By default, these two downloaded files
are cached under `$HOME/.cache/huggingface/transformers/`, which one may change
if they specify the `HF_HOME` environment variable otherwise.

**(?)** The files in `HF_HOME` are all named using unrecognizable, sha-1-like filenames.
How could we know which one is which?

**(R)** One way is to print the content of the JSON files to stdout.
```bash
$ ls ~/.cache/huggingface/transformers/*.json
/home/phunc20/.cache/huggingface/transformers/dc462194780c4638f894e183eec0e214c2891e32a0276d8437e019b6cafd4961.49eeeaed2051802f574bb8508bc9b90ddd068743c7b9c17dd1afcc18c5fc82fd.json
/home/phunc20/.cache/huggingface/transformers/ff1931049683ee1e934397a712f4202c59537de2fc0266e3587404cb18822f16.1a981b4b6ba73bb1d630760e2c7baf5bc300ce297d5bd57068fbaed633cc09f1.json

$ cat ~/.cache/huggingface/transformers/ff1931049683ee1e934397a712f4202c59537de2fc0266e3587404cb18822f16.1a981b4b6ba73bb1d630760e2c7baf5bc300ce297d5bd57068fbaed633cc09f1.json
{"url": "https://huggingface.co/microsoft/layoutlm-base-uncased/resolve/main/tokenizer_config.json", "etag": "\"252f4f7fbbe3ae65d76212dec8087988c856f024\""}
$ cat ~/.cache/huggingface/transformers/dc462194780c4638f894e183eec0e214c2891e32a0276d8437e019b6cafd4961.49eeeaed2051802f574bb8508bc9b90ddd068743c7b9c17dd1afcc18c5fc82fd.json
{"url": "https://huggingface.co/cl-tohoku/bert-base-japanese-v2/resolve/main/vocab.txt", "etag": "\"9ae1a39a04b4cdbae77b4652ab1cb8fbd54cd2b9\""}
```

To systematically find the targeted checkpoint, one could write a shell script like the one below.
```bash
for json in $(ls ~/.cache/huggingface/transformers/*.json); do
  echo $(basename "$json")
  cat $json
  printf "\n\n"
done
```


