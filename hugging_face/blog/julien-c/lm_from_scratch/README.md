


```
.
├── code
│   ├── 01_as_is
│   │   ├── 01_train.ipynb
│   │   ├── 01_train_Kaggle.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── trash.py
│   └── 02_as_nlp_course
│       └── 02_train_mlm
│           ├── 01_ordinary_masking.ipynb
│           ├── 01_ordinary_masking_Kaggle.ipynb
│           └── mlruns
├── data
│   ├── corbeille
│   │   └── oscar.eo.txt
│   └── oscar.eo.txt
└── README.md
```


## Failures
- `code/01_as_is/`
    - `01_train.ipynb` can be run locally/aws ec2, but not guaranteed to success
    - Too costly to reproduce the same Python environment (Rust, transformers versions) on Kaggle/Colab
- `code/02_as_nlp_course/01_ordinary_masking_Kaggle.ipynb` lr not descending, rubbish mlm results.
  Potential workarounds:
    1. Change `lr`
    1. Try with HF GitHub repo's Colab:
        - <https://github.com/huggingface/transformers/tree/main/examples/pytorch>
        - <https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/language_modeling.ipynb>
    1. Try with HF GitHub repo's scripts, e.g.
        - <https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_mlm.py>
