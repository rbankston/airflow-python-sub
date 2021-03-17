#FROM quay.io/astronomer/ap-airflow-dev:2.0.1-buster-onbuild-32688
FROM quay.io/astronomer/ap-airflow:2.0.0-buster-onbuild

USER root

RUN sed -i "s/from airflow.settings import CAN_FORK/CAN_FORK = False/" /usr/local/lib/python3.7/site-packages/airflow/task/task_runner/standard_task_runner.py


USER astro
