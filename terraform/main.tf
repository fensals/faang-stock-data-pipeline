# main.tf

# 

provider "google" {
  #credentials = #google credentials have been set in the environment variable GOOGLE_APPLICATION_CREDENTIALS
  project     = "faang-stock-pipeline"
  region      = "us-central1"  # or your preferred region
}


# Provision GCS bucket
resource "google_storage_bucket" "faang_bucket" {
  name     = "faang-stock-bucket"
  location = "US"
  storage_class = "STANDARD"
}

# Provision BigQuery dataset
resource "google_bigquery_dataset" "faang_dataset" {
  dataset_id = "faang_stock_dataset"
  project    = "faang-stock-pipeline"
  location   = "US"
}


