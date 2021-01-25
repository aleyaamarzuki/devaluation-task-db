"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class CondData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID              = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    restartTime         = Column(Text(length=10000))
    session             = Column(Text(length=10000))
    taskSession         = Column(Text(length=10000))
    taskSessionTry      = Column(Text(length=10000))
    stimCondTrack       = Column(Text(length=10000))
    totalTrialLog1 = Column(Text(length=10000))
    totalTrialLog2 = Column(Text(length=10000))
    totalTrialLog3 = Column(Text(length=10000))
    trialPerBlockNumLog1 = Column(Text(length=10000))
    trialPerBlockNumLog2 = Column(Text(length=10000))
    trialPerBlockNumLog3 = Column(Text(length=10000))
    stimIndexLog1 = Column(Text(length=10000))
    stimIndexLog2 = Column(Text(length=10000))
    stimIndexLog3 = Column(Text(length=10000))
    attenIndexLog1 = Column(Text(length=10000))
    attenIndexLog2 = Column(Text(length=10000))
    attenIndexLog3 = Column(Text(length=10000))
    totalBlockLog1 = Column(Text(length=10000))
    totalBlockLog2 = Column(Text(length=10000))
    totalBlockLog3 = Column(Text(length=10000))
    attenCheckAllLog1 = Column(Text(length=10000))
    attenCheckAllLog2 = Column(Text(length=10000))
    attenCheckAllLog3 = Column(Text(length=10000))
    outcomeLog1 = Column(Text(length=10000))
    outcomeLog2 = Column(Text(length=10000))
    outcomeLog3 = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_restartTime(self):
        return str(self.restartTime)

    def get_startTime(self):
        return str(self.taskSession)

    def get_restartTime(self):
        return str(self.taskSessionTry)

    def get_session(self):
        return str(self.session)

    def get_stimCondTrack(self):
        return str(self.stimCondTrack)

    def get_totalTrialLog1(self):
        return str(self.totalTrialLog1)

    def get_totalTrialLog2(self):
        return str(self.totalTrialLog2)

    def get_totalTrialLog3(self):
        return str(self.totalTrialLog3)

    def get_trialPerBlockNumLog1(self):
        return str(self.trialPerBlockNumLog1)

    def get_trialPerBlockNumLog2(self):
        return str(self.trialPerBlockNumLog2)

    def get_trialPerBlockNumLog3(self):
        return str(self.trialPerBlockNumLog3)

    def get_stimIndexLog1(self):
        return str(self.stimIndexLog1)

    def get_stimIndexLog2(self):
        return str(self.stimIndexLog2)

    def get_stimIndexLog3(self):
        return str(self.stimIndexLog3)

    def get_attenIndexLog1(self):
        return str(self.attenIndexLog1)

    def get_attenIndexLog2(self):
        return str(self.attenIndexLog2)

    def get_attenIndexLog3(self):
        return str(self.attenIndexLog3)

    def get_totalBlockLog1(self):
        return str(self.totalBlockLog1)

    def get_totalBlockLog2(self):
        return str(self.totalBlockLog2)

    def get_totalBlockLog3(self):
        return str(self.totalBlockLog3)

    def get_attenCheckAllLog1(self):
        return str(self.attenCheckAllLog1)

    def get_attenCheckAllLog2(self):
        return str(self.attenCheckAllLog2)

    def get_attenCheckAllLog3(self):
        return str(self.attenCheckAllLog3)

    def get_outcomeLog1(self):
        return str(self.outcomeLog1)

    def get_outcomeLog2(self):
        return str(self.outcomeLog2)

    def get_outcomeLog3(self):
        return str(self.outcomeLog3)

    def errors(self):
        errors = super(CondData, self).errors()
        return errors
