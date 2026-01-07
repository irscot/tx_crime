import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("houston_crime.csv", dtype=str)

# Convert date column
df["Occurrence Date"] = pd.to_datetime(df["Occurrence Date"], errors="coerce")

# Alcohol categories and their colors
alcohol_categories = {
    "Driving under the influence": "blue",
    "Liquor law violations": "red",
    "Drunkenness": "green"
}

plt.figure(figsize=(12, 6))

# Loop through each category and plot separately
for category, color in alcohol_categories.items():

    # Filter rows for this specific category
    mask = df["NIBRS Description"].str.contains(category, case=False, na=False)
    subset = df[mask].copy()

    # Group by month
    monthly_counts = (
        subset
        .groupby(subset["Occurrence Date"].dt.to_period("M"))
        .size()
    )

    # Plot this category
    plt.plot(
        monthly_counts.index.to_timestamp(),
        monthly_counts.values,
        label=category,
        color=color
    )

# Chart formatting
plt.title("Houston, TX – Alcohol-Related Crimes (Three Categories)")
plt.xlabel("Month")
plt.ylabel("Number of Incidents")
plt.legend(title="Crime Category")
plt.tight_layout()
plt.show()
