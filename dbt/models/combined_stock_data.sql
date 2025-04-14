SELECT
    'Facebook' AS Stock,
    Date,
    daily_average_price,
    total_volume
FROM `faang-stock-pipeline.faang_stock_dataset.facebook_model`
UNION ALL
SELECT
    'Apple' AS Stock,
    Date,
    daily_average_price,
    total_volume
FROM `faang-stock-pipeline.faang_stock_dataset.apple_model`
UNION ALL
SELECT
    'Amazon' AS Stock,
    Date,
    daily_average_price,
    total_volume
FROM `faang-stock-pipeline.faang_stock_dataset.amazon_model`
UNION ALL
SELECT
    'Netflix' AS Stock,
    Date,
    daily_average_price,
    total_volume
FROM `faang-stock-pipeline.faang_stock_dataset.netflix_model`
UNION ALL
SELECT
    'Google' AS Stock,
    Date,
    daily_average_price,
    total_volume
FROM `faang-stock-pipeline.faang_stock_dataset.google_model`