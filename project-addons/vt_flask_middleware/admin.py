# -*- coding: utf-8 -*-
"""
Admin dashboard.
Configures the admin interface.
"""

from flask_peewee.admin import Admin

from app import app
from auth import auth
from user import User
from product import Product
from customer import Customer

#
# Setup the admin interface.
#
admin = Admin(app, auth)
auth.register_admin(admin)

#
# Register the models available in the admin interface.
#
admin.register(User)
admin.register(Customer)
admin.register(Product)

# Enable the admin interface.
admin.setup()
