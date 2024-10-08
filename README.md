# Market Risk Monitoring - Stock Data Dashboard with Real-Time Risk Analysis

## Overview
This project is a web-based dashboard that visualizes stock data and performs real-time risk analysis. Users can input a company name or ticker symbol to fetch the latest stock data, including volatility, open prices, and close prices. The dashboard dynamically updates to display the current risk level based on statistical analysis.

## Features
- **Real-Time Data Fetching**: Enter a company name or ticker symbol to fetch and display real-time stock data.
- **Volatility Analysis**: Calculate and display stock price volatility.
- **Risk Assessment**: Automatically assess the risk level (Low, Medium, High) based on the stock's volatility.
- **Interactive Charts**: View stock data trends through interactive line charts.

## Live Demo
You can access the live demo of this project at [Market Risk Monitoring Dashboard](https://market-risk-monitoring.onrender.com).

## Technologies Used
- **Python**: Backend logic and data processing
- **Flask**: Web framework for serving the application
- **Alpha Vantage API**: Source of real-time stock data
- **Chart.js**: Frontend library for creating dynamic charts
- **HTML/CSS/JavaScript**: Frontend interface

## Installation

1. **Clone the Repository**:
    ```
    git clone https://github.com/yaseenbashat/market-risk-monitoring.git
    cd market-risk-monitoring
    ```

2. **Install Required Packages**:
    ```
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```
    python main.py
    ```

4. **Access the Dashboard**:
   Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage
- Enter a company name or ticker symbol in the input field.
- Click "Get Data" to fetch and visualize the stock data.
- View the real-time risk assessment and interactive stock charts.

## Contribution
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- **Alpha Vantage** for providing the stock data API.
- **Chart.js** for the charting library used in this project.
