Cf. <https://huggingface.co/docs/datasets/en/upload_dataset#upload-with-python>

1. `pip install huggingface_hub` in a virtual environment of your choice
1. On a terminal (emulator), do `huggingface-cli login`
    - This will ask for your **HuggingFace token**. If you haven't had one,
      please sign up a new account and obtain a token.
1. Use the `push_to_hub()` function to help you add, commit, and push a file
   to your repository, e.g.
   ```python
   >>> from datasets import load_dataset

   >>> dataset = load_dataset("imagefolder", data_dir="/home/phunc20/git-repos/huggingface_hub/phunc20/nj_biergarten_captcha_v2", drop_labels=True)

   >>> dataset.push_to_hub

   >>> dataset
   DatasetDict({
       train: Dataset({
           features: ['image'],
           num_rows: 20000
       })
       validation: Dataset({
           features: ['image'],
           num_rows: 300
       })
       test: Dataset({
           features: ['image'],
           num_rows: 500
       })
   })

   >>> dataset.push_to_hub("phunc20/nj_biergarten_captcha_v2")
   ```
    - Note that, if you forget to `huggingface-cli login` before starting your Python/IPython session, it **doesn't matter**!
      It suffices to login in another shell and the related Python code is smart enough to authenticate.
    - If you don't want people other than yourself to be able to use the dataset,
      add `private=True` to `push_to_hub()`.
