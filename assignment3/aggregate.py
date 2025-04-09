import pandas as pd

df = pd.read_csv("input/Food_Inspections_50k.csv")

agg_df = (
    df.groupby("Facility_Type")
    .size()
    .reset_index(name="Count")
    .sort_values("Facility_Type", ascending=True)
)

agg_df.to_csv("results/pandas-fac-types.csv", index=False)
