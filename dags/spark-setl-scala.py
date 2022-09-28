from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

#params
spark_master = "spark://10.0.9.226:7077"
now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
        dag_id="spark-setl", 
        description="This DAG for SETL frw.",
        default_args=default_args, 
        schedule_interval=None
    )

spark_job_load_postgres = SparkSubmitOperator(
    task_id="spark_job_setl",
    # application="/home/hoaln/work/git_clone/clone_project/all_setl/new_airflow_spark/airflow-spark/spark/resources/jars/setl_2.12-1.0.0-SNAPSHOT.jar",
    application="hdfs://10.0.9.226:8020/jars/setl_2.12-1.0.0-SNAPSHOT.jar",
    # name="load-postgres",
    # java_class='src.main.scala.Job_s2t_AddTagVideo',
    conn_id="spark_default",
    # verbose=1,
    conf={"spark.master" : "spark://10.0.9.226:7077"},
    # application_args=[movies_file,ratings_file,postgres_db,postgres_user,postgres_pwd],
    # jars='/home/hoaln/work/git_clone/clone_project/all_setl/new_airflow_spark/airflow-spark/spark/resources/jars/setl_2.12-1.0.0-SNAPSHOT-jar-with-dependencies.jar',
    jars='hdfs://10.0.9.226:8020/jars/setl_2.12-1.0.0-SNAPSHOT-jar-with-dependencies.jar',
    # driver_class_path='Job_s2t_AddTagVideo',
    dag=dag)