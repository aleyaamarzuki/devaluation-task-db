"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class Bonus(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    phase1Contin         = Column(Text(length=10000))
    phase2Contin         = Column(Text(length=10000))
    phase3Contin         = Column(Text(length=10000))
    phase1FbProb         = Column(Text(length=10000))
    phase2FbProb         = Column(Text(length=10000))
    phase3FbProb         = Column(Text(length=10000))
    bonus1               = Column(Text(length=10000))
    bonus2               = Column(Text(length=10000))
    bonus3               = Column(Text(length=10000))
    totalBonus           = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_contin_1(self):
        return str(self.phase1Contin)

    def get_contin_2(self):
        return str(self.phase2Contin)

    def get_contin_3(self):
        return str(self.phase3Contin)

    def get_fbProb_1(self):
        return str(self.phase1FbProb)

    def get_fbProb_2(self):
        return str(self.phase2FbProb)

    def get_fbProb_3(self):
        return str(self.phase3FbProb)

    def get_bonus_1(self):
        return str(self.bonus1)

    def get_bonus_2(self):
        return str(self.bonus2)

    def get_bonus_3(self):
        return str(self.bonus3)

    def get_total_bonus(self):
        return str(self.totalBonus)

    def errors(self):
        errors = super(Bonus, self).errors()
        return errors
