from flask import Flask, send_file
from flask_cors import CORS
import io
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

from data_handler import load_data, get_bmw_data, get_subaru_and_toyota_data, get_cumulative_growth, get_german_growth, get_supercar_growth

app = Flask(__name__)
CORS(app)

# Load and process data
df_full = load_data()
bmw_cars = get_bmw_data(df_full)
brz_86_combined = get_subaru_and_toyota_data(df_full)
model_counts = get_cumulative_growth(brz_86_combined)
german_brand_counts = get_german_growth(df_full)
supercar_brand_counts = get_supercar_growth(df_full)

@app.route('/api/bmw/top', methods=['GET'])
def get_bmw_top():
    plt.figure(figsize=(10, 5))
    sns.countplot(data=bmw_cars, x='model', order=bmw_cars['model'].value_counts().index[:10])
    plt.title('Top BMW Models (2015-2024)')
    plt.xticks(rotation=45)
    plt.xlabel('Model')
    plt.ylabel('Number of Registrations')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/api/bmw/least', methods=['GET'])
def get_bmw_least():
    plt.figure(figsize=(10, 5))
    sns.countplot(data=bmw_cars, x='model', order=bmw_cars['model'].value_counts().index[-5:])
    plt.title('Top 5 Least Registered BMW Models (2015-2024)')
    plt.xticks(rotation=45)
    plt.xlabel('Model')
    plt.ylabel('Number of Registrations')
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/api/brz_86', methods=['GET'])
def get_brz_86():
    plt.figure(figsize=(10, 5))
    sns.countplot(data=brz_86_combined, x='model', order=brz_86_combined['model'].value_counts().index)
    plt.title('Subaru BRZ vs Toyota 86 vs Toyota GR86')
    plt.xlabel('Model')
    plt.ylabel('Number of Registrations')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/api/cumulative_growth', methods=['GET'])
def get_cumulative_growth():
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=model_counts, x='year', y='cumulative_count', hue='model', marker='o')
    plt.title('Cumulative Growth of Subaru BRZ, Toyota 86 and Toyota GR86 (2015-2024)')
    plt.xlabel('Year')
    plt.ylabel('Counts')
    plt.legend(title='Model')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')


@app.route('/api/german_cars', methods=['GET'])
def get_conti_growth():
    img = io.BytesIO()
    plt.figure(figsize=(11, 5))

    conti_brand, conti_brand_yearly = get_german_growth(df_full)
    
    plot = sns.lineplot(data=conti_brand_yearly, x='year', y='cumulative_count', hue='model', marker='o')
    plt.title("German Makers with Top 3 Car Models")
    plt.xlabel("Year")
    plt.ylabel("Cumulative Count")

    min_year = 2014
    max_year = 2025
    plot.set_xlim(min_year, max_year)
    plot.xaxis.set_major_locator(mdates.YearLocator())
    plot.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xticks(rotation=45)
    plt.grid(True)

    ticks = [year for year in range(min_year, max_year + 1)]
    plot.set_xticks(ticks)  # Set x-axis ticks to be at each year
    plot.set_xticklabels(ticks)  # Ensure labels match the ticks

    handles, labels = plot.get_legend_handles_labels()
    cumulative_counts = conti_brand_yearly.groupby('model')['cumulative_count'].max()
    label_to_count = {label: cumulative_counts[label] for label in labels}
    sorted_labels_handles = sorted(zip(labels, handles), key=lambda x: label_to_count[x[0]], reverse=True)
    sorted_labels, sorted_handles = zip(*sorted_labels_handles)

    plt.legend(sorted_handles, sorted_labels, title='Model', bbox_to_anchor=(1.135, 1), loc='upper right')

    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/api/supercars', methods=['GET'])
def get_supercar_growth():
    img = io.BytesIO()

    plt.figure(figsize=(10,5))
    plot = sns.lineplot(data=supercar_brand_counts, x='year', y='cumulative_count', hue='model', marker='o')
    plt.title("Supercar Makers with Top 3 Car Models")
    plt.xlabel("Year")
    plt.ylabel("Cumulative Count")

    cumulative_counts = supercar_brand_counts.groupby('model')['cumulative_count'].max()

    handles, labels = plot.get_legend_handles_labels()
    label_to_count = {label: cumulative_counts[label] for label in labels}
    sorted_labels_handles = sorted(zip(labels, handles), key=lambda x: label_to_count[x[0]], reverse=True)
    sorted_labels, sorted_handles = zip(*sorted_labels_handles)

    plt.legend(sorted_handles, sorted_labels, title='Model', bbox_to_anchor=(1.135, 1), loc='upper right')
    plt.grid(True)
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png') 

if __name__ == '__main__':
    app.run(debug=True)
