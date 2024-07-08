import pandas as pd

# URL to the Parquet file
URL_DATA = 'https://storage.data.gov.my/transportation/cars_2024.parquet'

# Read the Parquet file into a pandas DataFrame
df = pd.read_parquet(URL_DATA)

# Convert 'date' column to datetime if it exists
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

print(df)
