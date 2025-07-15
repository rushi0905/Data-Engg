select * from new_sales_data;

CREATE TABLE new_sales_data (
    id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    amount DECIMAL(10, 2),
    last_updated DATETIME
);

----------------------------------------------------------

-- use case 8


CREATE TABLE products_1 (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100)
);

INSERT INTO products_1 (product_id, product_name, category) VALUES
(101, 'Smartphone', 'Electronics'),
(102, 'Blender', 'Home Appliances'),
(103, 'LED Bulb', 'Electronics'),
(104, 'Rice', 'Grocery'),
(105, 'Vacuum Cleaner', 'Home Appliances');

----------------------------------------------------------
-- use case 9


CREATE TABLE extended_sales_data (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    region VARCHAR(50),
    sale_amount DECIMAL(10,2),
    quantity INT,
    sale_date DATE
);

CREATE INDEX idx_product_date ON extended_sales_data (product_id, sale_date);
CREATE INDEX idx_sale_date ON extended_sales_data (sale_date);
CREATE INDEX idx_region ON extended_sales_data (region);
CREATE INDEX idx_customer_id ON extended_sales_data (customer_id);


-- Test query with filtering and grouping
EXPLAIN
SELECT product_id, SUM(sale_amount)
FROM extended_sales_data
WHERE sale_date BETWEEN '2024-01-01' AND '2024-06-30'
GROUP BY product_id;

----------------------------------------------------------
-- use case 11
ALTER TABLE extended_sales_data 
ADD COLUMN latitude VARCHAR(20),
ADD COLUMN longitude VARCHAR(20),
ADD COLUMN location_description TEXT;
