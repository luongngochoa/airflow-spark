from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

# class = 'Job_s2t_AddTagVideo'
now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    # "email": ["airflow@airflow.com"],
    "email": ["airflowadmin@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    dag_id="spark-setl1",
    description="This DAG for SETL frw test 2",
    default_args=default_args,
    schedule_interval=None
)

spark_job_load_postgres = SparkSubmitOperator(
    task_id="spark_job_setl1",
    # application="hdfs://10.0.9.226:8020/jars/setl_2.12-1.0.0-SNAPSHOT.jar",
    application="/home/hoaln/work/jars/setl_2.12-1.0.0-SNAPSHOT.jar",
    java_class="Job_s2t_AddTagVideo",
    conn_id="spark_default3",
    jars='/home/hoaln/work/jars/setl_2.12-1.0.0-SNAPSHOT-jar-with-dependencies.jar',
    # jars='hdfs://10.0.9.226:8020/jars/setl_2.12-1.0.0-SNAPSHOT-jar-with-dependencies.jar',
    name=None,
    dag=dag
)
