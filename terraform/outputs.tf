# outputs.tf

output "faang_stock_bucket" {
  value = google_storage_bucket.faang_bucket.name
}

output "faang_stock_dataset" {
  value = google_bigquery_dataset.faang_dataset.dataset_id
}
