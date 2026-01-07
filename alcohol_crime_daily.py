import pandas as pd
import matplotlib.pyplot as plt

# Load everything as strings to avoid dtype warnings
# Loading dataset as strings to avoid dtype warnings and ensure consistent string matching.
# Public crime datasets often contain mixed data types, so dtype=str keeps things predictable.
df = pd.read_csv("houston_crime.csv", dtype=str)

# Defining the alcohol-related keywords exactly as it appears in the dataset.
# Using case=False allows matching regardless of capitalization.
# Alcohol-related keywords found in NIBRS Description.
alcohol_keywords = {
    "Driving under the influence",
    "Liquor law violations",
    "Drunkenness"
}

drug_keywords = ["Drug, narcotic violations", "Drug equipment violations"]

# Filtering the dataset to only the NIBRS Description column.
# Creating a boolean mask that identifies rows where the NIBRS Description
# contains the alcohol-related keyword.
# 'na=False' prevents errors on missing values.
mask = df["NIBRS Description"].str.contains(
    "|".join(alcohol_keywords),
    case=False,
    na=False,
)

# Making new data frame that is separate from the original.
# Applying the mask to filter the dataset.
# .copy() ensures we get a fully independent DataFrame and avoids pandas' SettingWithCopyWarning.
alcohol_df = df[mask].copy()

# Converting occurred date column.
# Converting the Occurrence Date column from text into actual datetime objects.
# errors="coerce" turns invalid or missing dates into NaT instead of raising errors.
alcohol_df["Occurrence Date"] = pd.to_datetime(alcohol_df["Occurrence Date"], errors="coerce")

# Grouping by day
# .dt.to_period("D") converts each date into a Year-Day period for better visualization across the year 2025.
daily_counts = alcohol_df.groupby(alcohol_df["Occurrence Date"].dt.to_period("D")).size()

# Plotting data.
plt.plot(daily_counts.index.to_timestamp(), daily_counts.values, label=alcohol_keywords)

# Plotting the daily trend of DUI incidents
# Using line chart to easily see increases, decreases, and seasonal patterns.
daily_counts.plot(kind="line", figsize=(12, 6), title="Houston, TX - Daily Alcohol-Related Crimes in 2025")
plt.xlabel("Month")
plt.ylabel("Number of Incidents")
plt.ylim(0, 50) # setting y-axis limits from 0 to 50

plt.show()
