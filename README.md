
# Stock Market Analysis using SLURM

This project performs stock market data analysis using the SLURM workload manager to parallelize the fetching and calculation of stock indicators such as **Moving Averages** and **Relative Strength Index (RSI)**.

## Setup Instructions

### 1. Install Dependencies
- Install SLURM on controller and compute nodes.
- Install Python 3.x and the following Python libraries:
  - `yfinance`
  - `pandas`
  - `numpy`

### 2. Run the Project
- Place stock symbols in the SLURM job scripts (e.g., **AAPL**, **MSFT**).
- Use SLURM to parallelize the stock data fetching and analysis on compute nodes.
- Merge results on the controller node using the `merge_results.py` script.

## Project Structure
- `scripts/` : Contains Python scripts and SLURM job scripts.
- `data/` : Folder to store stock data (CSV files).
- `final_report.csv` : Merged results from all stock symbols.
