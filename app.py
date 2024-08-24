from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client['stock_data_db']
collection = db['stocks']

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch data
@app.route('/data')
def data():
    stock_data = list(collection.find().sort('timestamp', -1).limit(100))
    for data in stock_data:
        data['_id'] = str(data['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)
