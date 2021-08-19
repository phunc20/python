
## Logging Level
`logging.basicConfig(level=logging.DEBUG)` can be used to adjust the logging level.

The levels in increasing severity are

01. `DEBUG`
02. `INFO`
03. `WARNING` (default)
04. `ERROR`
05. `CRITICAL`

When we set the level to `sth`, then all logging messages of severity level higher or
equal to `sth` will be output to `stderr` (or to a log file if we configured so).
By default, `WARNING, ERROR, CRITICAL` will be output.
