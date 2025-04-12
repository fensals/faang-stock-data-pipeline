# variables.tf

variable "faang-stock-pipeline" {
  description = "The ID of the project"
  type        = string
}

variable "faang-stock-bucket" {
  description = "The name of the GCS bucket"
  type        = string
}

variable "faang_stock_dataset" {
  description = "The name of the BigQuery dataset"
  type        = string
}