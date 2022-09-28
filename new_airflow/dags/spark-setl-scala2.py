from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

#params
# spark_master = "spark://10.0.9.226:7077"
# spark_master = "spark://spark:7077"
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
        dag_id="spark-setl2", 
        description="This DAG for SETL frw test 2",
        default_args=default_args, 
        schedule_interval=None
    )

spark_job_load_postgres = SparkSubmitOperator(
    task_id="spark_job_setl2",
    application="/home/hoaln/work/git_clone/clone_project/all_setl/new_airflow_spark/airflow-spark/spark/resources/jars/setl_2.12-1.0.0-SNAPSHOT.jar",
    # application="hdfs://10.0.9.226:8020/jars/setl_2.12-1.0.0-SNAPSHOT.jar",
    conn_id="spark_default3",
    # verbose=1,
    # conf={"spark.master" : spark_master},
    jars='/home/hoaln/work/git_clone/clone_project/all_setl/new_airflow_spark/airflow-spark/spark/resources/jars/setl_2.12-1.0.0-SNAPSHOT-jar-with-dependencies.jar',
    # jars='hdfs://10.0.9.226:8020/jars/setl_2.12-1.0.0-SNAPSHOT-jar-with-dependencies.jar',
    dag=dag)