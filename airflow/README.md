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
