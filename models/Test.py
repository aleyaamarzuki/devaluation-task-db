"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text
from models.db import Model
from models.base_object import BaseObject

class Test(BaseObject, Model):
    id = Column(Integer, primary_key=True)
    userID = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)
    def get_userID(self):
        return str(self.userID)
    def errors(self):
        errors = super(Test, self).errors()
        return errors
