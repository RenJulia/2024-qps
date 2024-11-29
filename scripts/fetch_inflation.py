# scripts/fetch_inflation.py
import pandas_datareader.data as web
import pandas as pd
from datetime import datetime
import os
import sys
#print(sys.path)
# 将 'src' 目录添加到 Python 路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from data_utils import fetch_cpi_data, calculate_inflation


def main():
    # Fetch CPI data
    cpi_data = fetch_cpi_data()
    
    # Calculate inflation
    inflation_data = calculate_inflation(cpi_data)
    
    # Get the last 4 quarters of inflation
    last_4_quarters = inflation_data.tail(4)
    
    print("Last 4 quarters of US inflation:")
    print(last_4_quarters)

if __name__ == "__main__":
    main()
