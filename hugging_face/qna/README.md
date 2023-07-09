# Q&A
1. Learning rate scheduler
    - <https://dev.classmethod.jp/articles/huggingface-usage-scheluder-type/>
    - <https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py>
    - <https://huggingface.co/transformers/v4.2.2/_modules/transformers/trainer_utils.html#SchedulerType>
      ```python
      class SchedulerType(ExplicitEnum):
         LINEAR = "linear"
         COSINE = "cosine"
         COSINE_WITH_RESTARTS = "cosine_with_restarts"
         POLYNOMIAL = "polynomial"
         CONSTANT = "constant"
         CONSTANT_WITH_WARMUP = "constant_with_warmup"
      ```
    - <https://www.kaggle.com/code/rhtsingh/guide-to-huggingface-schedulers-differential-lrs>
    - <https://huggingface.co/transformers/v4.2.2/main_classes/optimizer_schedules.html#transformers.SchedulerType>
1. mlm
    - Data collator (`collate_fn`, etc.) and their `numpy_mask_tokens, tf_mask_tokens, torch_mask_tokens` functions:
        - <https://huggingface.co/docs/transformers/main_classes/data_collator#transformers.DataCollatorForLanguageModeling.numpy_mask_tokens>
        - <https://github.com/huggingface/transformers/blob/v4.30.0/src/transformers/data/data_collator.py#L806>
