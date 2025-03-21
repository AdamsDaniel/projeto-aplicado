from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/risk_management'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return jsonify({"message": "API is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
