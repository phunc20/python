```bash
source /path_to_your_conda_install/etc/profile.d/conda.sh 
```

```bash
#/bin/bash
echo "which python\n$(which python)"
echo "which python3\n$(which python3)"
echo

eval "$(conda shell.bash hook)"
echo "eval \$(conda shell.bash hook)"
conda activate huggingface
echo condact huggingface
echo "which python\n$(which python)"
echo "which python3\n$(which python3)"

#python run_image_classification.py \
#    --dataset_name ./orientation \
#    --train_dir train.zip \
#    --output_dir ./outputs/ \
#    --remove_unused_columns False \
#    --do_train \
#    --do_eval


python run_image_classification.py \
    --dataset_config_name orientation/orientation.py \
    --output_dir ./outputs/ \
    --remove_unused_columns False \
    --do_train \
    --do_eval
```
