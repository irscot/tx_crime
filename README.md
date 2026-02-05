---

# 📘 README

## Houston Crime Data: Alcohol‑Related Incident Analysis

This project analyzes Houston crime data to identify and visualize **alcohol‑related offenses** over time. The script filters relevant incidents, converts date fields, aggregates monthly counts, and plots trends using a line chart.

---

## Requirements

- Python 3  
- pandas  
- matplotlib  

Install dependencies:

```bash
pip install pandas matplotlib
```

---

## How the Script Works

### **1. Load the Dataset**
The script loads `houston_crime.csv` using `dtype=str` to avoid mixed‑type warnings and ensure consistent string matching.

### **2. Identify Alcohol‑Related Crimes**
A set of keywords is defined to match alcohol‑related offenses in the **NIBRS Description** column.  
A boolean mask filters rows containing any of these keywords.

### **3. Create a Filtered DataFrame**
The filtered subset is copied into a new DataFrame (`alcohol_df`) to avoid `SettingWithCopyWarning`.

### **4. Convert Dates**
The `Occurrence Date` column is converted to datetime format using `errors="coerce"` to safely handle invalid entries.

### **5. Aggregate Monthly Counts**
Incidents are grouped by **Year‑Month** using `.dt.to_period("M")`, producing a monthly time‑series count.

### **6. Plot the Trend**
A line chart visualizes the number of alcohol‑related crimes per month, with labeled axes and a fixed y‑axis range for readability.

---

## Output

- A line plot showing monthly alcohol‑related crime trends in Houston  
- Aggregated monthly counts of filtered incidents  

---
