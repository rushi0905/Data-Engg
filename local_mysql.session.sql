select * from new_sales_data;

CREATE TABLE new_sales_data (
    id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    amount DECIMAL(10, 2),
    last_updated DATETIME
);
