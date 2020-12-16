"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class VolCal(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID     = Column(Text(length=10000))
    date       = Column(Text(length=10000))
    startTime   = Column(Text(length=10000))
    volCalStage= Column(Text(length=10000))
    checkTry   = Column(Text(length=10000))
    qnTime      = Column(Text(length=10000))
    qnRT       = Column(Text(length=10000))
    qnNum       = Column(Text(length=10000))
    soundIndex  = Column(Text(length=10000))
    soundFocus  = Column(Text(length=10000))
    volume      = Column(Text(length=10000))
    volumePer   = Column(Text(length=10000))
    volumeNotLog = Column(Text(length=10000))
    playNum     = Column(Text(length=10000))
    quizAnsIndiv = Column(Text(length=10000))
    qnPressKey  = Column(Text(length=10000))
    qnCorrIndiv = Column(Text(length=10000))
    averRating  = Column(Text(length=10000))
    arouRating  = Column(Text(length=10000))
    averRatingDef= Column(Text(length=10000))
    arouRatingDef= Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_volCalStage(self):
        return str(self.volCalStage)

    def get_checkTry(self):
        return str(self.checkTry)

    def get_qnTime(self):
        return str(self.qnTime)

    def get_qnRT(self):
        return str(self.qnRT)

    def get_qnNum(self):
        return str(self.qnNum)

    def get_soundIndex(self):
        return str(self.soundIndex)

    def get_soundFocus(self):
        return str(self.soundFocus)

    def get_volume(self):
        return str(self.volume)

    def get_volumePer(self):
        return str(self.volumePer)

    def get_volumeNotLog(self):
        return str(self.volumeNotLog)

    def get_playNum(self):
        return str(self.playNum)

    def get_quizAnsIndiv(self):
        return str(self.quizAnsIndiv)

    def get_qnPressKey(self):
        return str(self.qnPressKey)

    def get_qnCorrIndiv(self):
        return str(self.qnCorrIndiv)

    def get_averRating(self):
        return str(self.averRating)

    def get_arouRating(self):
        return str(self.arouRating)

    def get_averRatingDef(self):
        return str(self.averRatingDef)

    def get_arouRatingDef(self):
        return str(self.arouRatingDef)

    def errors(self):
        errors = super(VolCal, self).errors()
        return errors
