import pandas as pd

sql_df = pd.read_csv("results/sql-fac-types.csv")
pandas_df = pd.read_csv("results/pandas-fac-types.csv")

print("SQL columns:", sql_df.columns.tolist())
print("Pandas columns:", pandas_df.columns.tolist())

sql_df_sorted = sql_df.sort_values(by="Facility_Type").reset_index(drop=True)
pandas_df_sorted = pandas_df.sort_values(by="Facility_Type").reset_index(drop=True)

pandas_df_sorted = pandas_df_sorted[sql_df_sorted.columns]

if sql_df_sorted.equals(pandas_df_sorted):
    comparison = pd.DataFrame(columns=["No Differences"])
else:
    comparison = sql_df_sorted.compare(pandas_df_sorted)
    
comparison.to_csv("results/comparison.csv", index=False)
