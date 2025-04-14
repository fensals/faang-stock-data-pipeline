# FAANG Stock Data Pipeline

## Objective
The goal of this project is to apply the concepts learned in the Data Zoomcamp to build an end-to-end data pipeline for processing, transforming, and visualizing stock data for Facebook, Apple, Amazon, Netflix, and Google.

## Problem Statement
Stock market data is essential for analyzing trends and making informed investment decisions. This project aims to:
- Download FAANG stock data (Facebook, Apple, Amazon, Netflix, and Google) from [Kaggle](https://www.kaggle.com/datasets/aayushmishra1512/faang-complete-stock-data)
- Store the data in a datalake (Google cloud bucket) for batch processing.
- Move the cleaned data to a data warehouse (Bigquery) for transformation and optimized querying.
- Transform the data using dbt to prepare it for reporting.
- Build a dashboard for visualization


## Technologies Used
#### Cloud: Google Cloud Platform (GCP)
- Data Lake: Google Cloud Bucket
- Data Warehouse: BigQuery
- Dashboarding Tool: Looker Studio

#### Infrastructure as Code (IaC): Terraform
- Used for provisioning cloud resources such as the Google Cloud Storage bucket, BigQuery dataset, and other GCP components in a programmatic and reproducible way.

#### Workflow Orchestration: Apache Airflow
- Automates the steps in the pipeline using a Directed Acyclic Graph (DAG).

#### Transformations: dbt (Data Build Tool)
- Executes SQL-based transformations and creates optimized tables in BigQuery.

#### Containerization: Docker
- Used to ensure a reproducible environment for running the pipeline locally and in the cloud.



Pipeline Architecture
The pipeline is batch-based and executes the following steps:
- Data Ingestion:- Python script (download_upload_load.py) fetches FAANG stock data and stores it in a datalake (Google Cloud Storage).
- Dockerized Airflow orchestrates this step.

- Data Warehousing:- Data is loaded from the datalake into BigQuery for efficient querying.

- Data Transformation:- dbt models transform raw data into structured tables with calculated metrics such as daily_average_price and total stock volume
- Optimizations like table partitioning and clustering are implemented.

- Dashboarding:- Looker Studio was used to visualize the data.




Flow Diagram
Below is a simplified representation of the DAG used in the project:


![Flow Diagram](https://raw.githubusercontent.com/fensals/FAANG-STOCK-DATA-PIPELINE/refs/heads/master/dashboard/flow_diagram.png)



Dashboard
The final dashboard contains:
- A Line Chart showing the daily average price of each stock over the specified period.
- A Bar Chart showing the Total trading volume for each stock
- A tile each for Facebook, Apple, Amazon, Netflix, and Google showing their highest stock price in that period.

  ![Dashboard](https://raw.githubusercontent.com/fensals/FAANG-STOCK-DATA-PIPELINE/refs/heads/master/dashboard/viz.png)

Access the dashboard [here](https://lookerstudio.google.com/reporting/bd538abc-0f63-46c1-83a3-8ef9a2662f93)

Setup Instructions
Follow these steps to reproduce the pipeline:

- Clone Repository:
```git clone https://github.com/fensals/FAANG-STOCK-DATA-PIPELINE.git```
```cd FAANG-STOCK-DATA-PIPELINE```

- Setup Environment:- Install Docker
- Build and run the Docker containers:```docker-compose up --build```

- Run Airflow DAG:- Access the Airflow web interface at http://localhost:8080.
- The running docker container will trigger the DAG named faang_stock_pipeline_dag.

- Verify BigQuery Tables:- Check your BigQuery dataset (faang_stock_dataset) for the transformed tables.

- View Dashboard:- Open the Looker Studio dashboard via the provided link.



## Future Plans

#### - Machine Learning Model for Stock Price Prediction
- I Plan to build a machine learning model to predict FAANG stock prices using Google Cloud’s machine learning tools.
- Will explore services such as Vertex AI (Google Cloud’s unified ML platform) to create and deploy the model.

#### Reworking the Project on Azure
- Recreate this pipeline using Microsoft Azure as the cloud platform.
- Use Azure Data Lake, Azure Synapse Analytics, and other Azure services for data ingestion, warehousing, and dashboarding or just use Microsoft Fabric.

#### Exploring Alternative Orchestration Tools
- I intend to Experiment with Prefect as an orchestration tool to compare its features and ease of use with Apache Airflow.




