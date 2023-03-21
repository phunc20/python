## Usage
The scripts
- `asynchr.py`
- `naive.py`
- `process_pool.py`
- `thread_pool.py`

could all be executed like follows:
```bash
python asynchr.py
```
without needing to add any arguments.  
The only thing which needs to be modified is the
variable `pdf_dir` in each script. Please specify
a directory of PDF files on your local machine.

Each such scripts, when successfully finished running,
will generate a file named `profiling_eval_yyyymmdd-hhmmss.prof`,
which one could visualize by `snakeviz`. (`pip install snakeviz`
to install it.)
