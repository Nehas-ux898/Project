import pandas as pd
import glob

csv_files = glob.glob("*.csv")  # Load all stock CSV files
final_df = pd.concat([pd.read_csv(file) for file in csv_files])

final_df.to_csv("final_report.csv", index=False)
print("Final report generated: final_report.csv")
