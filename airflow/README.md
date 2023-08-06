# `airflow==2.6.3`
## Installation of Airflow
After installing and activating
a virtual environment,
`pip install` Airflow as follows.
```shell
AIRFLOW_VERSION=2.6.3
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[postgres]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```


## Initialize An Airflow Database
1. Set the environment variable `AIRFLOW_HOME`
1. Run the command `airflow db init`
    - N.B. This command will create the directory
      `AIRFLOW_HOME/` if it has not yet created,
      and will put in there the following files and folders
      ```
      airflow.cfg
      airflow.db
      logs
      webserver_config.py
      ```

For example,
```shell
$ export AIRFLOW_HOME="/tmp/air_jordan"
$ conda activate airflow_apprentice
(airflow_apprentice) $ airflow db init
(airflow_apprentice) $ ls /tmp/air_jordan/
airflow.cfg  airflow.db  logs  webserver_config.py
```

If one does not set `AIRFLOW_HOME` then it will default to
`$HOME/airflow/` of the current user. A good alternative
is `export AIRFLOW_HOME="$HOME/.config/airflow/"`


## Dags
- `default_args` seems to want to refer to the default args of
  the **operators** instead of of the dag itself. For example,
  a typical `default_args` could look like
  ```python
  default_args = {
      "owner": "Ranga",
      "start_date": datetime(2023, 8, 5),
      "retries": 3,
      "retry_delay": timedelta(seconds=10),
  }
  ```
  And if you look into the docs, then you'll find
  ```python
  In [1]: from airflow.operators.empty import EmptyOperator
  
  In [2]: EmptyOperator?
  EmptyOperator(
      task_id: 'str',
      owner: 'str' = 'airflow',
      email: 'str | Iterable[str] | None' = None,
      email_on_retry: 'bool' = True,
      email_on_failure: 'bool' = True,
      retries: 'int | None' = 0,
      retry_delay: 'timedelta | float' = datetime.timedelta(seconds=300),
      start_date: 'datetime | None' = None,
  ```
  That is, `default_args` is a convenient way to DRY.
- `schedule_interval: str` is sth similar to crontab format
  `m h dom m dow`.
  Cf. <https://wiki.archlinux.org/title/cron#Crontab_format> for more info
- `catchup: bool`
    - When set to `True`
      (and when `start_date` is set to a date in the past),
      will run or **catch up** all the tasks from the past to current date
    - When set to `False`, will not run past tasks


## Operators/Tasks
- It seems that both `<<` and `>>` could be used to indicate **order**/**dependency**
  of the tasks, so, for example
  ```python
  task2 << task1 << task0
  ```
  seems to be equiv. to
  ```python
  task0 >> task1 >> task2
  ```


## Terminologies
- An **operator** is a Python class and a **task** is an instance of an operator
- Users.  
  It seems that, by default, there is no users whatsoever, so without having
  created any user, one simply cannot login into the Web UI.
  ```shell
  (airflow_apprentice) $ airflow users list
  No data found
  (airflow_apprentice) $ 
  ```
  One can create a new user and specify its password easily with
  `airflow users create`. Cf. `airflow users create --help`  
  To delete a user, cf. `airflow users delete --help`
      - The `AIRFLOW_HOME` env var is important here. The created user will
        be saved into `AIRFLOW_HOME/airflow.db`. Make sure you are saving
        the right user to the right database
      - If you do not type the password from stdin, then Airflow will
        ask you the user's password later, masking what you type for security
