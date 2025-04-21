from app import create_app  
from app.extensions import db
from app.models.user import User
from app.models.manager import Manager
from app.models.chef import Chef
from app.models.sales_clerk import SalesClerk

# Initialize the app and database
app = create_app()

# Create tables manually
with app.app_context():
    db.create_all()
