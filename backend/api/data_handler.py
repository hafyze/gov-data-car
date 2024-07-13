import pandas as pd

def load_data():
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

    if dfs:
        df_full = pd.concat(dfs, ignore_index=True)
        print("Concatenation successful.")
    else:
        df_full = pd.DataFrame()
        print("Error in concatenation.")

    if 'date_reg' in df_full.columns:
        df_full['date_reg'] = pd.to_datetime(df_full['date_reg'])

    return df_full

def get_bmw_data(df):
    return df[df['maker'] == "BMW"]

def get_subaru_and_toyota_data(df):
    subaru_cars = df[df['maker'] == 'Subaru']
    toyota_cars = df[df['maker'] == 'Toyota']

    subaru_brz = subaru_cars[subaru_cars['model'] == 'BRZ']
    toyota_86 = toyota_cars[toyota_cars['model'] == "86"]
    toyota_GR86 = toyota_cars[toyota_cars['model'] == "GR86"]

    return pd.concat([subaru_brz, toyota_86, toyota_GR86])

def get_cumulative_growth(df):
    df['year'] = df['date_reg'].dt.year
    model_counts = df.groupby(['year', 'model']).size().reset_index(name='count')
    model_counts['cumulative_count'] = model_counts.groupby('model')['count'].cumsum()
    return model_counts

def get_german_growth(df):
    brands = ["BMW", "Mercedes Benz", "Audi"]
    top_models = {}

    for brand in brands:
        brand_data = df[df['maker'] == brand]
        top_models[brand] = brand_data['model'].value_counts().nlargest(3).index.tolist()

    top_models_data = df[df['model'].isin(sum(top_models.values(), []))].copy()  

    top_models_data.loc[:, 'year'] = top_models_data['date_reg'].dt.year
    conti_brand = top_models_data.groupby(['year', 'model']).size().reset_index(name='count')
    conti_brand['cumulative_count'] = conti_brand.groupby('model')['count'].cumsum()

    return conti_brand
