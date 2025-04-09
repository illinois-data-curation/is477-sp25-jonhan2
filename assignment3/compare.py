import pandas as pd

sql_df = pd.read_csv("results/sql-fac-types.csv")
pandas_df = pd.read_csv("results/pandas-fac-types.csv")

comparison = sql_df.compare(pandas_df)
comparison.to_csv("results/comparison.csv")
