from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
 
# Default arguments for the DAG
default_args = {
    'owner': 'team4',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 28),  # Adjust as needed
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
 
# Define the DAG
with DAG(

    'boardgame_etl',
    default_args=default_args,
    description='ETL pipeline for board game data using Spark and Airflow',
    schedule_interval='@daily',
    catchup=False,
) as dag:
    command = """
    export JAVA_HOME=/opt/java/openjdk;
    /opt/spark/bin/spark-submit --master spark://spark-leader:7077 /opt/spark/work-dir/etl.py; 
    """
    run_spark_etl = SSHOperator(
        task_id='run_spark_etl',
        ssh_conn_id='spark_ssh',  # Make sure to set up this connection in Airflow
        command=command,
        dag=dag,
        cmd_timeout=600
    )

run_spark_etl