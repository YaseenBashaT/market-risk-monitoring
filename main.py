import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# Initialize the API and fetch the data
API_key = 'AJR2QAEL3BVPAE0B'
ts = TimeSeries(key=API_key, output_format='pandas')
data, meta_data = ts.get_monthly_adjusted('F')

# Example: Calculate the volatility
data['volatility'] = ((data['2. high'] - data['3. low']) / data['3. low']) * 100

# Statistical analysis: Calculate mean and standard deviation of volatility
mean_volatility = data['volatility'].mean()
std_volatility = data['volatility'].std()

# Set threshold: e.g., High risk is when volatility is more than 2 standard deviations above the mean
high_risk_threshold = mean_volatility + 2 * std_volatility
medium_risk_threshold = mean_volatility + 1 * std_volatility

# Assign risk levels based on thresholds
def calculate_risk(row):
    if row['volatility'] > high_risk_threshold:
        return 'High Risk'
    elif row['volatility'] > medium_risk_threshold:
        return 'Medium Risk'
    else:
        return 'Low Risk'


# Display the data with risk levels
print(data[['volatility']])

