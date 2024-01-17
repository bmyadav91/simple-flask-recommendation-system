# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Read data from the CSV file
csv_file_path = 'myntra_products_catalog.csv'
data = pd.read_csv(csv_file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input
    user_input = request.form['user_input'].lower()

    # Simple content-based recommendation
    recommendations = get_recommendations(user_input, data)

    # Limit the results to a maximum of 10 recommendations
    recommendations = recommendations[:10]

    return jsonify({'recommendations': recommendations})

def get_recommendations(user_input, data):
    # Simple matching based on product descriptions
    user_input_lower = user_input.lower()
    
    # Filter products that contain the user input in the description
    matching_products = [product['ProductName'] for _, product in data.iterrows() if user_input_lower in str(product['Description']).lower()]

    return matching_products

if __name__ == '__main__':
    app.run(debug=True)
