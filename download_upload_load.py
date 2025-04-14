import os
import kagglehub
from google.cloud import storage, bigquery

# Step 1: Download the dataset from Kaggle
dataset = kagglehub.dataset_download("aayushmishra1512/faang-complete-stock-data")
print(f"Dataset downloaded to: {dataset}")

# Step 2: Upload to Google Cloud Storage
client = storage.Client()
bucket_name = "faang-stock-bucket"  # Replace with your GCS bucket name
bucket = client.get_bucket(bucket_name)

# Loop over the files in the downloaded directory and upload them
for filename in os.listdir(dataset):
    file_path = os.path.join(dataset, filename)
    if os.path.isfile(file_path):
        blob = bucket.blob(f"faang-stock-data/{filename}")  # GCS path where the files will be stored
        blob.upload_from_filename(file_path)
        print(f"Dataset uploaded to GCS: gs://{bucket_name}/faang_stock_dataset/{filename}")

# Step 3: Load data into BigQuery
client_bq = bigquery.Client()
dataset_id = "faang_stock_dataset"  # BigQuery dataset
#table_id_prefix = "faang_stock_dataset_"  # Prefix for the table names

# Loop over the files again and load them into BigQuery
for filename in os.listdir(dataset):
    file_path = os.path.join(dataset, filename)
    if os.path.isfile(file_path):
        gcs_uri = f"gs://{bucket_name}/faang-stock-data/{filename}"
        table_id = f"{filename.split('.')[0]}"  # Create a table for each CSV file

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            autodetect=True,
        )

        with open(file_path, "rb") as source_file:
            load_job = client_bq.load_table_from_file(source_file, f"{dataset_id}.{table_id}", job_config=job_config)
            load_job.result()  # Wait for the load job to complete

        print(f"Dataset {filename} loaded into BigQuery table {table_id}")
