"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TutorialData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID              = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    tutorialSession     = Column(Text(length=10000))
    tutorialSessionTry  = Column(Text(length=10000))
    trialNum            = Column(Text(length=10000))
    trialTime           = Column(Text(length=10000))
    fixTime             = Column(Text(length=10000))
    attenIndex          = Column(Text(length=10000))
    attenCheckKey       = Column(Text(length=10000))
    attenCheckTime      = Column(Text(length=10000))
    stimTime            = Column(Text(length=10000))
    stimIndex           = Column(Text(length=10000))
    fbProbTrack         = Column(Text(length=10000))
    randProb            = Column(Text(length=10000))
    responseKey         = Column(Text(length=10000))
    reactionTime        = Column(Text(length=10000))
    playFbSound         = Column(Text(length=10000))
    fbTime              = Column(Text(length=10000))
    volume              = Column(Text(length=10000))
    volumeNotLog        = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_userID(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_tutorial_session(self):
        return str(self.tutorialSession)

    def get_tutorial_session_try(self):
        return str(self.tutorialSessionTry)

    def get_trial_no(self):
        return str(self.trialNum)

    def get_trial_time(self):
        return str(self.trialTime)

    def get_fix_time(self):
        return str(self.fixTime)

    def get_atten_index(self):
        return str(self.attenIndex)

    def get_attencheck_key(self):
        return str(self.attenCheckKey)

    def get_attencheck_time(self):
        return str(self.attenCheckTime)

    def get_stim_time(self):
        return str(self.stimTime)

    def get_stim_index(self):
        return str(self.stimIndex)

    def get_fb_prob(self):
        return str(self.fbProbTrack)

    def get_rand_prob(self):
        return str(self.randProb)

    def get_response_key(self):
        return str(self.responseKey)

    def get_reaction_time(self):
        return str(self.reactionTime)

    def get_response_avoid(self):
        return str(self.responseAvoid)

    def get_fb_sound(self):
        return str(self.playFbSound)

    def get_fb_time(self):
        return str(self.fbTime)

    def get_volume(self):
        return str(self.volume)

    def get_volumeNotLog(self):
        return str(self.volumeNotLog)

    def errors(self):
        errors = super(TutorialData, self).errors()
        return errors
