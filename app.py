from flask import Flask, render_template, request, jsonify
from logic import process_order

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    order_data = request.json
    result = process_order(order_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
