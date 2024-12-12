from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Order
import os

# Configuration Class
class Config:
    # Database URI for AWS RDS PostgreSQL
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:DevOps2024*@database-3.cdug00k6kj78.us-east-1.rds.amazonaws.com/webappdb?sslmode=require'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configurations from Config class

    db.init_app(app)  # Initialize database with Flask app

    # Ensure all tables are created in the database
    with app.app_context():
        db.create_all()

    return app

app = create_app()

# Route to display all products
@app.route('/')
def index():
    products = Product.query.all()  # Fetch all products from the database
    return render_template('index.html', products=products)

# Route to add a new product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            stock_quantity = int(request.form['stock_quantity'])

            # Create a new Product object
            product = Product(name=name, description=description, price=price, stock_quantity=stock_quantity)

            # Add to the database
            db.session.add(product)
            db.session.commit()

            return redirect(url_for('index'))
        except Exception as e:
            return str(e)  # Handle any errors gracefully

    return render_template('add_product.html')

# Route to view product details
@app.route('/view_product/<int:product_id>')
def view_product(product_id):
    # Fetch the product or return 404 if not found
    product = Product.query.get_or_404(product_id)
    return render_template('view_product.html', product=product)

# Route to place an order
@app.route('/order/<int:product_id>', methods=['POST'])
def order_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)

        # Calculate the order details
        quantity = int(request.form['quantity'])
        total_price = product.price * quantity

        # Create and save the Order object
        order = Order(product_id=product_id, quantity=quantity, total_price=total_price)
        db.session.add(order)
        db.session.commit()

        return redirect(url_for('index'))
    except Exception as e:
        return str(e)  # Handle errors in order creation gracefully

if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for development
