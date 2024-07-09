import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from 2015 to 2024
years = range(2015, 2025)
dfs = []

for year in years:
    url = f'https://storage.data.gov.my/transportation/cars_{year}.parquet'
    try:
        df = pd.read_parquet(url)
        dfs.append(df)
        print(f"Data for {year} loaded successfully.")
    except Exception as e:
        print(f"Failed to load data for {year}: {e}")

# Concatenate dataframes
if dfs:
    df_full = pd.concat(dfs, ignore_index=True)
    print("Concatenation successful.")
else:
    df_full = pd.DataFrame()
    print("Error in concatenation.")

# Data Overview
print("\n=Null Data Value=")
print(df_full.isnull().sum())

# Filter for BMW cars
bmw_cars = df_full[df_full['maker'] == "BMW"]

# Visualizing Top BMW Models (2015-2024)
plt.figure(figsize=(14, 8))
sns.countplot(data=bmw_cars, x='model', order=bmw_cars['model'].value_counts().index[:10])
plt.title('Top BMW Models (2015-2024)')
plt.xticks(rotation=45)
plt.xlabel('Model')
plt.ylabel('Number of Registrations')
plt.show()

# Filter data for BMW cars
bmw_cars = df_full[df_full['maker'] == "BMW"]

# Distribution of 'model' for BMW cars
plt.figure(figsize=(14, 7))
sns.countplot(data=bmw_cars, x='model', order=bmw_cars['model'].value_counts().index[-5:])
plt.title('Top 5 Least Registered BMW Models (2015-2024)')
plt.xticks(rotation=45) 
plt.xlabel('Model')
plt.ylabel('Number of Registrations')
plt.tight_layout()
plt.show()