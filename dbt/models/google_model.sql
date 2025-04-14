WITH google_data AS (
  SELECT
      CAST(Date AS DATE) AS Date,  -- Ensuring Date is in the correct format
      CAST(Open AS FLOAT64) AS Open,  -- Casting Open to FLOAT64
      CAST(High AS FLOAT64) AS High,  -- Casting High to FLOAT64
      CAST(Low AS FLOAT64) AS Low,    -- Casting Low to FLOAT64
      CAST(Close AS FLOAT64) AS Close,  -- Casting Close to FLOAT64
      CAST(`Adj Close` AS FLOAT64) AS `Adj Close`,  -- Casting Adj Close to FLOAT64
      CAST(Volume AS INT64) AS Volume   -- Casting Volume to INT64 (as it should be numeric)
  FROM
      `faang-stock-pipeline.faang_stock_dataset.Google`
  WHERE
      Date BETWEEN DATE('2012-06-01') AND DATE('2020-06-30')  -- Filtering for data from June 2012 to June 2020
)

SELECT
    Date,
    Open,
    High,
    Low,
    Close,
    `Adj Close`,
    Volume,
    (Open + High + Low + Close) / 4 AS daily_average_price,  -- Calculating daily average price
    SUM(Volume) OVER () AS total_volume  -- Total volume across the entire time period
FROM
    google_data
