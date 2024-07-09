import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Concatenate dataframes (18-23)
if dfs:
    df_full = pd.concat(dfs, ignore_index=True)
    print("Concatenation successful.")
else:
    df_full = pd.DataFrame()
    print("Error in concatenation.")

# Convert Data (25-30)
if 'date_reg' in df_full.columns:
    df_full['date_reg'] = pd.to_datetime(df_full['date_reg'])

for column in ['type', 'maker', 'model', 'colour', 'fuel', 'state']:
    df_full[column] = df_full[column].astype('category')

# Data Overview
print("\n=Null Data Value=")
print(df_full.isnull().sum())

# Filter for BMW
bmw_cars = df[df['maker'] == "BMW"]

# Visualising Top BMW
plt.figure(figsize=(14, 10))
sns.countplot(data=bmw_cars, x='model', order=bmw_cars['model'].value_counts().index)
plt.title('Top BMW Models (2015-2024)')
plt.xticks(rotation=90)
plt.show()


## Predictive QUESTIONS: 
#   - 