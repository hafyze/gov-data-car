from flask import Flask, jsonify, send_file
from flask_cors import CORS
import io
import matplotlib.pyplot as plt
import seaborn as sns

from data_handler import load_data, get_bmw_data, get_subaru_and_toyota_data, get_cumulative_growth

app = Flask(__name__)
CORS(app)

# Load and process data
df_full = load_data()
bmw_cars = get_bmw_data(df_full)
brz_86_combined = get_subaru_and_toyota_data(df_full)
model_counts = get_cumulative_growth(brz_86_combined)

@app.route('/api/bmw/top', methods=['GET'])
def get_bmw_top():
    plt.figure(figsize=(14, 8))
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
    plt.figure(figsize=(14, 7))
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
    plt.figure(figsize=(14, 8))
    sns.countplot(data=brz_86_combined, x='model', order=brz_86_combined['model'].value_counts().index)
    plt.title('Subaru BRZ vs Toyota 86 vs Toyota GR86')
    plt.xlabel('Model')
    plt.ylabel('Number of registration')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/api/cumulative_growth', methods=['GET'])
def get_cumulative_growth():
    plt.figure(figsize=(14, 8))
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

if __name__ == '__main__':
    app.run(debug=True)
