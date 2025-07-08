DESC EMPLOYEES_NEW;
CREATE TABLE Employees_new (
    EMPLOYEE_ID NUMBER(6),      -- Up to 6 digits
    NAME        VARCHAR2(20),   -- String up to 20 characters
    SALARY      NUMBER(8,2)     -- Up to 8 digits, 2 after decimal
);

INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (100, 'Jennifer', 4400);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (101, 'Michael', 13000);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (102, 'Pat', 6000);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (103, 'Den', 11000);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (104, 'Alexander', 3100);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (105, 'Shelli', 2900);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (106, 'Sigel', 2800);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (107, 'Guy', 2600);
INSERT INTO Employees_new (EMPLOYEE_ID, NAME, SALARY) VALUES (108, 'Karen', 2500);

select max(salary) as salary from EMPLOYEES_NEW where salary not in (select max(salary) as salary from EMPLOYEES_NEW);
WITH temp AS (
    SELECT MAX(salary) AS max_salary
    FROM EMPLOYEES_NEW
)
SELECT MAX(salary) AS second_highest_salary
FROM EMPLOYEES_NEW
WHERE salary < (SELECT max_salary FROM temp);select a.*from EMPLOYEES_NEW a join temp b on a.salary = b.salary;

select salary from (select salary from EMPLOYEES_NEW order by salary desc) where ROWNUM < 3;

select max(salary) as salary from EMPLOYEES_NEW where salary not in (select salary from (select salary from EMPLOYEES_NEW order by salary desc) where ROWNUM < 3); 
-- OR
