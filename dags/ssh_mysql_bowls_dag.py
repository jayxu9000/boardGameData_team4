import pendulum
from airflow.decorators import dag
from airflow.providers.ssh.operators.ssh import SSHOperator


@dag(
    schedule_interval=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def ssh_mysql_bowls_dag():
    command = """
    export JAVA_HOME=/opt/java/openjdk;
    /opt/spark/bin/spark-submit --master spark://spark-leader:7077 /opt/spark/work-dir/mysql_bowls_app.py; 
    """
    ssh_task = SSHOperator(
        ssh_conn_id="ssh_leader", task_id="ssh_task", command=command, cmd_timeout=600
    )

    ssh_task


ssh_mysql_bowls_dag()
