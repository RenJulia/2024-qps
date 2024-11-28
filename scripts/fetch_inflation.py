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


def fetch_cpi_data():
    """
    Fetch the US CPI (Consumer Price Index) data from the FRED database.
    """
    cpi_data = web.DataReader('CPIAUCNS', 'fred', start=datetime(2000, 1, 1))
    return cpi_data

def calculate_inflation(cpi_data):
    """
    Calculate the quarterly inflation rate based on the CPI data.
    """
    # Resample data to quarterly frequency and calculate the percentage change
    cpi_quarterly = cpi_data.resample('Q').last()
    cpi_quarterly['Inflation'] = cpi_quarterly['CPIAUCNS'].pct_change() * 100
    return cpi_quarterly

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
