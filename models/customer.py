from uuid import uuid4

from mongoengine import *


class Customer(Document):
    _id = UUIDField(default=uuid4, primaryKey=True)
    fiscal_number = StringField(max_length=10, unique=True, required=True, indexed=True)

