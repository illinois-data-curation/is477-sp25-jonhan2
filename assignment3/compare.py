import pandas as pd

# Load and sort both DataFrames
sql_df = pd.read_csv("results/sql-fac-types.csv").sort_values(by="Facility_Type").reset_index(drop=True)
pandas_df = pd.read_csv("results/pandas-fac-types.csv").sort_values(by="Facility_Type").reset_index(drop=True)

# Reorder columns to match
pandas_df = pandas_df[sql_df.columns]

# Check equality
if sql_df.equals(pandas_df):
    # Write a simple message indicating no differences
    pd.DataFrame([["No Differences"]]).to_csv("results/comparison.csv", index=False, header=False)
else:
    # Show both DataFrames side-by-side to highlight differences
    merged = pd.concat(
        [sql_df.add_suffix("_SQL"), pandas_df.add_suffix("_Pandas")], axis=1
    )
    merged.to_csv("results/comparison.csv", index=False)
