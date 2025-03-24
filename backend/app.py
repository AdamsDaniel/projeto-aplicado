from flask import Flask, jsonify, request # Erro de importação somente no projeto local
from flask_sqlalchemy import SQLAlchemy # Erro de importação somente no projeto local

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/risk_management'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return jsonify({"message": "API is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
