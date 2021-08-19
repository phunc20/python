
```bash
(oft) ~/.../python/logging/log_file_and_stderr$ ls
default.py  README.md  stderr.py  stdout.py
(oft) ~/.../python/logging/log_file_and_stderr$ python default.py
DEBUG:root:default debug
INFO:root:default info
WARNING:root:default warning
ERROR:root:default error
(oft) ~/.../python/logging/log_file_and_stderr$ python stderr.py
This message should go to the log file
So should this
And this, too
And non-ASCII stuff, too, like Øresund and Malmö
(oft) ~/.../python/logging/log_file_and_stderr$ cat err.log
DEBUG:root:This message should go to the log file
INFO:root:So should this
WARNING:root:And this, too
ERROR:root:And non-ASCII stuff, too, like Øresund and Malmö
(oft) ~/.../python/logging/log_file_and_stderr$ python stdout.py
stdout debug
stdout info
stdout warning
stdout error
(oft) ~/.../python/logging/log_file_and_stderr$ cat out.log
DEBUG:root:stdout debug
INFO:root:stdout info
WARNING:root:stdout warning
ERROR:root:stdout error
```
