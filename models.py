from flask_sqlalchemy import SQLAlchemy

# Initialize the db instance
db = SQLAlchemy()

# Define the Product model
class Product(db.Model):
    __tablename__ = 'product'  # Explicitly set the table name

    id = db.Column(db.Integer, primary_key=True)  # Primary key column for product
    name = db.Column(db.String(100), nullable=False)  # Ensure name is not null
    description = db.Column(db.Text)  # Description of the product, can be null
    price = db.Column(db.Float, nullable=False)  # Price of the product, cannot be null
    stock_quantity = db.Column(db.Integer, nullable=False)  # Quantity of the product in stock, cannot be null

    def __repr__(self):
        return f"<Product {self.name}>"

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the order
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)  # Foreign key reference to product
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of the ordered product
    total_price = db.Column(db.Float, nullable=False)  # Total price for the order
    status = db.Column(db.String(50), default='Pending')  # Status, default to 'Pending'

    # Relationship with Product model, lazy loading of orders related to a product
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"<Order {self.id}>"
