
`load_dataset()` supports a wide variety of file format and converts them
into `Dataset` object. Cf. <https://huggingface.co/docs/datasets/loading> for more info.
- `.txt`: Use, for example, `load_dataset("text", data_files="path/to/your/file.txt")`.
  ```python
  In [1]: from datasets import load_dataset
  
  In [2]: !cat abc.txt
  excruciating adj. Causing great pain or anguish, agonizing
  clay n. An earth material with ductile qualities
  ductile adj. Capable of being pulled or stretched into thin wire by mechanical force without breaking.
  
  In [3]: en_dictionary = load_dataset("text", data_files="abc.txt")
  Using custom data configuration default-cf99d97e98eb2e6d
  Downloading and preparing dataset text/default to /home/phunc20/.cache/huggingface/datasets/text/default-cf99d97e98eb2e6d/0.0.0/4b86d3
  14f7236db91f0a0f5cda32d4375445e64c5eda2692655dd99c2dac68e8...
  Downloading data files: 100%|█████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 7169.75it/s]
  Extracting data files: 100%|██████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 1470.65it/s]
  Dataset text downloaded and prepared to /home/phunc20/.cache/huggingface/datasets/text/default-cf99d97e98eb2e6d/0.0.0/4b86d314f7236db9
  1f0a0f5cda32d4375445e64c5eda2692655dd99c2dac68e8. Subsequent calls will reuse this data.
  100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 236.85it/s]
  
  In [4]: en_dictionary
  Out[4]:
  DatasetDict({
      train: Dataset({
          features: ['text'],
          num_rows: 3
      })
  })
  
  In [5]: en_dictionary["train"][0]
  Out[5]: {'text': 'excruciating adj. Causing great pain or anguish, agonizing'}
  
  In [6]: en_dictionary["train"][1]
  Out[6]: {'text': 'clay n. An earth material with ductile qualities'}
  
  In [7]: en_dictionary["train"][2]
  Out[7]: {'text': 'ductile adj. Capable of being pulled or stretched into thin wire by mechanical force without breaking.'}
  ```

