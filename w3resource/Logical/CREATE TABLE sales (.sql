CREATE TABLE sales (
    order_id INT,
    product_id INT,
    sale_amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES
(1, 101, 250.00, '2023-01-15'),
(2, 102, 300.00, '2023-01-25'),
(3, 103, 150.00, '2023-02-10'),
(4, 104, 400.00, '2023-04-18'),
(5, 105, 200.00, '2023-05-22'),
(6, 106, 100.00, '2023-07-12'),
(7, 107, 350.00, '2024-01-20'),
(8, 108, 500.00, '2024-03-05');


select * from sales;

drop TABLE if exists sales;

-- Monthly Sales
SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(sale_amount) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;

--Quartely Sales
SELECT concat(YEAR(sale_date),'-Q',QUARTER(sale_date)) AS quarter,sum(sale_amount) as total_sales FROM sales GROUP BY QUARTER;

-- Yearly sales
SELECT YEAR(sale_date) as year ,sum(sale_amount) as total_sales from sales GROUP BY year;

CREATE index idx_sales_date on sales(sale_date);

DESCRIBE sales;

show index from sales;

-- Use case : 4
SELECT * FROM sales WHERE price IS NULL OR customer_name IS NULL;

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    product_id INT,
    customer_name VARCHAR(100),
    sale_amount DECIMAL(10, 2),
    quantity INT,
    sale_date DATE,
    region VARCHAR(50)
);

INSERT INTO sales (order_id, product_id, customer_name, sale_amount, quantity, sale_date, region) VALUES
(101, 1, 'Alice', 1000.00, 2, '2025-07-01', 'North'),
(102, 2, 'Bob', NULL, 1, '2025-07-02', 'South'),               -- NULL sale_amount
(103, 3, NULL, 850.00, 1, '2025-07-03', 'East'),               -- NULL customer_name
(104, 4, 'Charlie', -500.00, 1, '2025-07-04', 'West'),         -- Negative sale_amount
(105, 5, 'Diana', 1200.00, NULL, '2025-07-05', 'North'),       -- NULL quantity
(106, 6, 'Eva', 950.00, 1, NULL, 'South'),                     -- NULL sale_date
(107, 7, 'Frank', 1100.00, -2, '2025-07-07', 'East'),          -- Negative quantity
(108, 8, 'Grace', 990.00, 2, '2025-07-08', 'West');            -- Valid

SELECT * from sales;

-- SELECT * FROM sales where sale_amount as price and price IS NULL or  customer_name IS NULL;
with sales_with_price AS(SELECT sale_amount as price from sales ) SELECT * from sales_with_price where price is null or customer_name is null;

SELECT * from sales_with_price where  price < 0;

CREATE VIEW sales_with_price AS SELECT sale_amount as price , customer_name from sales;

update sales_with_price SET price = '0.0' WHERE price = NULL;

SELECT * from sales_with_price;

DELETE FROM sales WHERE price < 0;

-- USE case : 5

SELECT order_id,sale_amount,sale_date from sales;

-- Objective: Process data to compute daily averages and analyze trends.

-- A. Calculate Daily Average Sale
SELECT date(sale_date) as sale_day, AVG(sale_amount) as avg_daily_sales from sales GROUP BY sale_day;

-- B. Detect Sales Trends Over Tim
SELECT 
    sale_day,
    avg_daily_sales,
    LAG(avg_daily_sales) OVER (ORDER BY sale_day) AS previous_day_avg,
    avg_daily_sales - LAG(avg_daily_sales) OVER (ORDER BY sale_day) AS daily_change
FROM (
    SELECT 
        DATE(sale_date) AS sale_day,
        AVG(sale_amount) AS avg_daily_sales
    FROM sales
    GROUP BY sale_day
) AS daily_stats;

--   3. Load Step
--   Objective: Store the transformed insights for further use or visualization.

--  

CREATE TABLE daily_sales_trend AS
SELECT 
    sale_day,
    avg_daily_sales,
    previous_day_avg,
    daily_change
FROM (
    SELECT 
        sale_day,
        avg_daily_sales,
        LAG(avg_daily_sales) OVER (ORDER BY sale_day) AS previous_day_avg,
        avg_daily_sales - LAG(avg_daily_sales) OVER (ORDER BY sale_day) AS daily_change
    FROM (
        SELECT 
            DATE(sale_date) AS sale_day,
            AVG(sale_amount) AS avg_daily_sales
        FROM sales
        GROUP BY sale_day
    ) AS daily_stats
) AS trend_analysis;


-- Use case : 6

WITH sales_enriched AS (
    SELECT
        *,
        EXTRACT(YEAR FROM sale_date) AS year,
        EXTRACT(MONTH FROM sale_date) AS month
    FROM sales
),
mom_yoy_calc AS (
    SELECT
        sale_date,
        sale_amount,

        -- MoM: Previous sale by date order
        LAG(sale_amount) OVER (ORDER BY sale_date) AS prev_sale,
        sale_amount - LAG(sale_amount) OVER (ORDER BY sale_date) AS mom_growth,

        -- YoY: Compare with same month last year
        LAG(sale_amount) OVER (PARTITION BY EXTRACT(MONTH FROM sale_date)
                               ORDER BY sale_date) AS yoy_sale,
        sale_amount - LAG(sale_amount) OVER (PARTITION BY EXTRACT(MONTH FROM sale_date)
                                             ORDER BY sale_date) AS yoy_growth

    FROM sales_enriched
)

SELECT *
FROM mom_yoy_calc
ORDER BY sale_date;

