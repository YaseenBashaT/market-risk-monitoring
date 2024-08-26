from flask import Flask, render_template, request, jsonify
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

API_key = '4YBAZN65ICY5IIDD'
app = Flask(__name__)

# Function to fetch and process stock data
def get_stock_data(company):
    ts = TimeSeries(key=API_key, output_format='pandas')
    data, meta_data = ts.get_monthly_adjusted(company)

    # Calculate the volatility
    data['volatility'] = ((data['2. high'] - data['3. low']) / data['3. low']) * 100

    # Statistical analysis: Calculate mean and standard deviation of volatility
    mean_volatility = data['volatility'].mean()
    std_volatility = data['volatility'].std()

    # Set thresholds for risk levels
    high_risk_threshold = mean_volatility + 2 * std_volatility
    medium_risk_threshold = mean_volatility + 1 * std_volatility

    # Assign risk levels based on thresholds
    def calculate_risk(volatility):
        if volatility > high_risk_threshold:
            return 'High Risk'
        elif volatility > medium_risk_threshold:
            return 'Medium Risk'
        else:
            return 'Low Risk'

    # Prepare data for the frontend
    data['timestamp'] = data.index.strftime('%Y-%m-%d')  # Format the timestamp
    data['risk_level'] = data['volatility'].apply(calculate_risk)  # Calculate risk for each row

    # Convert the data to a dictionary format for JSON serialization
    stock_data = data[['timestamp', 'volatility', '1. open', '4. close', 'risk_level']].to_dict(orient='records')
    return stock_data

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch data based on the company name or ticker symbol
@app.route('/data')
def data_route():
    company = request.args.get('company', default='AAPL')  # Default to AAPL if no company is provided
    stock_data = get_stock_data(company)
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
