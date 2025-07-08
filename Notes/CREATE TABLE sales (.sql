CREATE TABLE sales (
    order_id INT,
    product_id INT,
    sale_amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (1, 101, 250.00, TO_DATE('2023-01-15', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (2, 102, 300.00, TO_DATE('2023-01-25', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (3, 103, 150.00, TO_DATE('2023-02-10', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (4, 104, 400.00, TO_DATE('2023-04-18', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (5, 105, 200.00, TO_DATE('2023-05-22', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (6, 106, 100.00, TO_DATE('2023-07-12', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (7, 107, 350.00, TO_DATE('2024-01-20', 'YYYY-MM-DD'));
INSERT INTO sales (order_id, product_id, sale_amount, sale_date) VALUES (8, 108, 500.00, TO_DATE('2024-03-05', 'YYYY-MM-DD'));


select
    date_format(sale_date,'%Y-%m') as month,
    SUM(sale_amount) as total_sales
    from SALES
    GROUP BY month ORDER by month; 