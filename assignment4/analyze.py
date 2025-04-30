import pandas as pd

# Load the dataset
df = pd.read_csv("food-inspections-dirty.csv")

# Count the number of unique DBA Names
num_unique_businesses = df["DBA Name"].nunique()

print("Number of distinct businesses:", num_unique_businesses)

# Drop NaN values from the Risk column
risk_clean = df["Risk"].dropna()

# Normalize capitalization and spacing
# Example: "  risk 1 (HIGH) " → "risk 1 (high)"
risk_clean = risk_clean.str.strip().str.lower()

# Count unique normalized Risk values
num_unique_risks = risk_clean.nunique()

print("Number of distinct Risk Levels:", num_unique_risks)

# Drop rows with NaN in the Violations column
violations_series = df["Violations"].dropna()

# Split each cell on the "|" symbol, strip whitespace, and flatten the list
all_violations = set()

for entry in violations_series:
    # Split on pipe and strip each individual violation
    split_violations = [v.strip() for v in entry.split("|")]
    all_violations.update(split_violations)

# Get the number of unique violations
print("Number of unique violations:", len(all_violations))

# Filter rows where Result is 'Fail'
fail_df = df[df["Results"].str.strip().str.lower() == "fail"]

# Drop rows with missing or malformed City State Zip
fail_df = fail_df[fail_df["City State Zip"].notna()]

# Extract Zip Code from "City State Zip" (assumes ZIP is the last item after splitting by ',')
fail_df["Zip"] = fail_df["City State Zip"].apply(lambda x: x.split(",")[-1].strip())

# Group by Zip code and count failures
fail_counts = fail_df["Zip"].value_counts()

# Get the Zip with the most Fail results
top_zip = fail_counts.idxmax()

print("Top-1 Zip code with most 'Fail' results:", top_zip)