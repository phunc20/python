## UTF-8
When one saves a dictionary into a JSON file using `json.dump()`, by default, unicode characters that are not ASCII
will be displayed with unicode code point. This may not be always convenient, e.g. when we want to examine the file
content using `vim`, `less`, `cat`, etc. The is an arg to change this: `ensure_ascii`. Cf. `lisible.py`

