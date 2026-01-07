import pandas as pd
import matplotlib.pyplot as plt

# Load everything as text to avoid dtype warnings
# Load the dataset as text to avoid dtype warnings and ensure consistent string matching.
# Public crime datasets often contain mixed data types, so dtype=str keeps things predict
df = pd.read_csv("houston_crime.csv", dtype=str)

# # Define the alcohol-related keyword exactly as it appears in the dataset.
# Using case=False allows matching regardless of capitalization.
# Alcohol-related keywords found in NIBRS Description
alcohol_keywords = {
    "Driving under the influence": "blue",
    "Liquor law violations": "red",
    "Drunkenness": "green"
}

drug_keywords = ["Drug, narcotic violations", "Drug equipment violations"]

# Filter only the NIBRS Description column
# Create a boolean mask that identifies rows where the NIBRS Description
# contains the alcohol-related keyword. 'na=False' prevents errors on missing values.
mask = df["NIBRS Description"].str.contains(
    "|".join(alcohol_keywords),
    case=False,
    na=False,
)

# making new data frame that is separate from the original
# Apply the mask to filter the dataset.
# .copy() ensures we get a fully independent DataFrame and avoids pandas' SettingWithCopyWarning.
alcohol_df = df[mask].copy()

# Convert occurred date column
# Convert the Occurrence Date column from text into actual datetime objects.
# errors="coerce" turns invalid or missing dates into NaT instead of raising errors.
alcohol_df["Occurrence Date"] = pd.to_datetime(alcohol_df["Occurrence Date"], errors="coerce")

# Group by month
# .dt.to_period("M") converts each date into a Year-Month period, ideal for time-series aggregation.
monthly_counts = alcohol_df.groupby(alcohol_df["Occurrence Date"].dt.to_period("M")).size()

# Plotting each category with its own color and label
plt.plot(monthly_counts.index.to_timestamp(), monthly_counts.values, label=alcohol_keywords)

# Plotting the monthly trend of DUI incidents
# Using line chart to easily see increases, decreases, and seasonal patterns.
monthly_counts.plot(kind="line", figsize=(12,6), title="Houston, TX - Alcohol-Related Crimes in 2025")
plt.xlabel("Month")
plt.ylabel("Number of Incidents")
plt.ylim(0, 500) # setting y-axis limits from 0 to 500

plt.show()
