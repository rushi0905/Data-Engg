'''
3. Aggregating Sales Data Over Different Time Periods
Objective: Generate reports for sales aggregated by month, quarter, and year.

Steps:
1. Extract sales data from the MySQL database.
2. Aggregate data by month, quarter, and year using SQL.
3. Display the results for reporting purposes.

Tasks:
- Use GROUP BY and HAVING to aggregate sales by different time periods.
- Implement query optimization techniques (e.g., indexing on date columns).
'''

from sqlalchemy import create_engine
import pandas as pd

def extract_sales_from_mysql(user, password, host, port, database, table) -> pd.DataFrame:
    """Extract sales data from MySQL table."""
    conn_str = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"   
     #"mysql+mysqlconnector://root:Admin%40123@localhost:3306/jvm
    engine = create_engine(conn_str)
    
    query = f"SELECT * FROM {table};"
    df = pd.read_sql(query, engine)
    print(df)
    # Ensure sale_date is datetime
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    return df


def add_time_dimensions(df: pd.DataFrame) -> pd.DataFrame:
    df['year'] = df['sale_date'].dt.year
    df['month'] = df['sale_date'].dt.to_period('M')
    df['quarter'] = df['sale_date'].dt.to_period('Q')
    return df

def aggregate_sales(df: pd.DataFrame, period: str) -> pd.DataFrame:
    if period == 'month':
        group_col = 'month'
    elif period == 'quarter':
        group_col = 'quarter'
    elif period == 'year':
        group_col = 'year'
    else:
        raise ValueError("Invalid period")

    result = df.groupby(group_col)['sale_amount'].sum().reset_index()
    result.columns = [f'sale_{period}', 'total_sales']
    return result

def run_etl_and_print_mysql():
    # Update with your actual database details
    user = "root"
    password = "Admin%40123"
    host = "localhost"
    port = 3306
    database = "jvm"
    table = "sales"
    
    # Extract
    df = extract_sales_from_mysql(user, password, host, port, database, table)
    
    # Transform
    df = add_time_dimensions(df)
    monthly = aggregate_sales(df, 'month')
    quarterly = aggregate_sales(df, 'quarter')
    yearly = aggregate_sales(df, 'year')
    
    # Load (Print here)
    print("=== Monthly Sales ===")
    print(monthly, '\n')

    print("=== Quarterly Sales ===")
    print(quarterly, '\n')

    print("=== Yearly Sales ===")
    print(yearly)

if __name__ == "__main__":
    run_etl_and_print_mysql()
