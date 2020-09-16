"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class AttenData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID = Column(Text(length=10000))
    tutorialSession = Column(Text(length=10000))
    tutorialSessionTry = Column(Text(length=10000))
    taskSession = Column(Text(length=10000))
    taskSessionTry = Column(Text(length=10000))
    attenTrial = Column(Text(length=10000))
    attenTime = Column(Text(length=10000))
    attenCheckKey = Column(Text(length=10000))
    attenCheckTime = Column(Text(length=10000))
    playAttCheck = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_tutorial_session(self):
        return str(self.tutorialSession)

    def get_tutorial_session_try(self):
        return str(self.tutorialSessionTry)

    def get_task_session(self):
        return str(self.taskSession)

    def get_task_session_try(self):
        return str(self.taskSessionTry)

    def get_atten_trial(self):
        return str(self.attenTrial)

    def get_atten_time(self):
        return str(self.attenTime)

    def get_atten_check_key(self):
        return str(self.attenCheckKey)

    def get_atten_check_time(self):
        return str(self.attenCheckTime)

    def get_play_atten_check(self):
        return str(self.playAttCheck)

    def errors(self):
        errors = super(AttenData, self).errors()
        return errors
