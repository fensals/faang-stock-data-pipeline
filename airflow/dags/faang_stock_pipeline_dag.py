from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator

from airflow.operators.python import PythonOperator

# Function to print step message
def print_step_message(step_name):
    print(f"Running {step_name}")

with DAG(
    dag_id="faang_stock_pipeline_dag",
    schedule_interval="@monthly",  
    start_date=datetime(2025, 13, 4),  
    catchup=False,  
    default_args={
        'retries': 3,
        'retry_delay': timedelta(minutes=5),  
    }
) as dag:

    # Add PythonOperator to print message for each step
    print_download_message = PythonOperator(
        task_id="print_download_message",
        python_callable=print_step_message,
        op_args=["Downloading and Uploading Data to GCS and BigQuery"]
    )

    print_check_data_message = PythonOperator(
        task_id="print_check_data_message",
        python_callable=print_step_message,
        op_args=["Checking Data in BigQuery"]
    )

    print_dbt_run_message = PythonOperator(
        task_id="print_dbt_run_message",
        python_callable=print_step_message,
        op_args=["Running DBT transformations"]
    )

    print_dbt_test_message = PythonOperator(
        task_id="print_dbt_test_message",
        python_callable=print_step_message,
        op_args=["Running DBT tests"]
    )

    download_upload_load = BashOperator(
        task_id="download_upload_load",
        bash_command="python /opt/dbt/download_upload_load.py",
    )

    check_data_loaded = BigQueryCheckOperator(
        task_id="check_data_loaded",
        sql="SELECT COUNT(*) FROM `faang-stock-pipeline.faang_stock_dataset.Facebook`",
        location="US",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/dbt && dbt run && exit 0",
    )


    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/dbt && dbt test",
    )

    # Set up the task dependencies with print steps
    print_download_message >> download_upload_load
    download_upload_load >> print_check_data_message >> check_data_loaded
    check_data_loaded >> print_dbt_run_message >> dbt_run
    dbt_run >> print_dbt_test_message >> dbt_test
    dbt_test >> print_step_message("Pipeline Completed")