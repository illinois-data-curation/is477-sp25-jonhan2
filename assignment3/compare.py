import pandas as pd

# Load and sort
sql_df = pd.read_csv("results/sql-fac-types.csv").sort_values(by="Facility_Type").reset_index(drop=True)
pandas_df = pd.read_csv("results/pandas-fac-types.csv").sort_values(by="Facility_Type").reset_index(drop=True)

# Ensure same columns, in same order
pandas_df = pandas_df[sql_df.columns]

# Align index explicitly
sql_df.index = range(len(sql_df))
pandas_df.index = range(len(pandas_df))

# Perform comparison safely
if sql_df.equals(pandas_df):
    pd.DataFrame([["No Differences"]]).to_csv("results/comparison.csv", index=False, header=False)
else:
    comparison = sql_df.compare(pandas_df)
    comparison.to_csv("results/comparison.csv", index=False)
