# 2024-qps: US Inflation Analysis

This repository contains the code to fetch US CPI data and analyze the last 4 quarters of inflation in the United States. The analysis is done using Python, Pandas, and Jupyter Notebook.

## GitHub Repository URL
https://github.com/RenJulia/2024-qps?tab=readme-ov-file

## How to Run the Code

Follow the steps below to set up the environment and run the code.

### Step 1: Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/Ren%20Julia/2024-qps.git
```

### Step 2: Set Up a Python Virtual Environment
It is recommended to use a virtual environment to avoid conflicts with other packages on your system. To create and activate the virtual environment, run the following commands:
```bash
cd 2024-qps
python3 -m venv myenv        # Create a virtual environment
source myenv/bin/activate    # Activate the virtual environment
```

### step 3: pip install
```bash
pip install pandas pandas_datareader jupyter
```

###  Step 4: Run the Script to Fetch US CPI Data
Now that the environment is set up, you can run the script to fetch US CPI data and calculate inflation:
```bash
python scripts/fetch_inflation.py
```

### Step 5: Run the Jupyter Notebook (Optional)
If you'd like to explore the analysis in a more interactive way, you can open the Jupyter Notebook:
```bash
jupyter notebook
```
This will open Jupyter in your browser, where you can open the notebooks stored in the notebooks/ directory and explore the data in an interactive way.

### Step 6: Deactivate the Virtual Environment
After you've finished working, deactivate the virtual environment by running:
```bash
deactivate
```