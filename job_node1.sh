#!/bin/bash
#SBATCH --job-name=stock_analysis_node1
#SBATCH --output=output_node1.log
#SBATCH --ntasks=2
#SBATCH --time=01:00:00

module load python
python ~/stock_analysis/scripts/stock_analysis.py AAPL &
python ~/stock_analysis/scripts/stock_analysis.py MSFT &
wait
