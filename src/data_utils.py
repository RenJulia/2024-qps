# src/data_utils.py
import pandas_datareader.data as web
from datetime import datetime

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
