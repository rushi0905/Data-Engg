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

----------------------------------------------------------
-- use case 12

CREATE TABLE customer_segments (
    customer_id INT PRIMARY KEY,
    recency INT,
    frequency INT,
    monetary DECIMAL(10,2),
    segment VARCHAR(20)
);

select * from customer_segments;

show tables;

----------------------------------------------------------
-- use case 13

CREATE TABLE employee_hierarchy_data (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    manager_id INT
);
INSERT INTO employee_hierarchy_data (emp_id, emp_name, manager_id)
VALUES (1, 'CEO', NULL),
    (2, 'VP Marketing', 1),
    (3, 'VP Sales', 1),
    (4, 'Sales Manager', 3),
    (5, 'Sales Executive', 4),
    (6, 'Marketing Manager', 2),
    (7, 'Marketing Executive', 6);

rename table employee_hierarchy_data to employee_hierarchy;

select * from employee_hierarchy;

----------------------------------------------------------
-- use case 13

CREATE TABLE batch_sales_summary (
    year INT,
    month INT,
    region VARCHAR(50),
    category VARCHAR(50),
    total_sales DECIMAL(10,2),
    total_quantity INT
);

----------------------------------------------------------
-- use case 14

drop table if exists products;

CREATE table products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    last_updated DATETIME
)

INSERT INTO products(product_id, product_name, category, price, last_updated) VALUES
(101, 'Running Shoes', 'Footwear', 2999.00, '2025-07-23 10:00:00'),
(102, 'Sports Watch', 'Accessories', 4999.00, '2025-07-23 12:00:00'),
(103, 'Yoga Mat', 'Fitness', 899.00, '2025-07-24 15:30:00'),
(104, 'Gym Gloves', 'Fitness', 499.00, '2025-07-25 09:00:00'),
(105, 'Water Bottle', 'Fitness', 299.00, '2025-07-25 10:15:00');

update products
set price = 999.00,
last_updated = '2025-07-25 11:00:00'
WHERE product_id=103;

INSERT INTO products (product_id, product_name, category, price, last_updated)
VALUES (106, 'Treadmill Oil', 'Fitness', 149.00, '2025-07-25 11:30:00');

SELECT * FROM products
WHERE last_updated > '2025-07-25 00:00:00';

----------------------------------------------------------
-- use case 15
show tables;

describe table customers;
show CREATE table customers;

