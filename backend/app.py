from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Change for PostgreSQL/MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    purchase_rate = db.Column(db.Float, nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sold_rate = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=datetime.date.today)

# Routes
@app.route('/add_brand', methods=['POST'])
def add_brand():
    data = request.json
    new_brand = Brand(name=data['name'], purchase_rate=data['purchase_rate'])
    db.session.add(new_brand)
    db.session.commit()
    return jsonify({'message': 'Brand added successfully'})

@app.route('/add_sale', methods=['POST'])
def add_sale():
    data = request.json
    brand = Brand.query.filter_by(name=data['brand']).first()
    if not brand:
        return jsonify({'error': 'Brand not found'}), 400
    
    new_sale = Sale(brand_id=brand.id, quantity=data['quantity'], sold_rate=data['sold_rate'])
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale recorded successfully'})

@app.route('/profit_report', methods=['GET'])
def profit_report():
    report_type = request.args.get('type', 'daily')
    today = datetime.date.today()
    
    if report_type == 'monthly':
        start_date = today.replace(day=1)
    elif report_type == 'yearly':
        start_date = today.replace(month=1, day=1)
    else:
        start_date = today
    
    sales = Sale.query.filter(Sale.date >= start_date).all()
    total_profit = 0
    for sale in sales:
        brand = Brand.query.get(sale.brand_id)
        profit = (sale.sold_rate - brand.purchase_rate) * sale.quantity
        total_profit += profit
    
    return jsonify({'total_profit': total_profit, 'report_type': report_type})

if __name__ == '__main__':
    with app.app_context():
      db.create_all()
    app.run(debug=True)
