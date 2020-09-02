"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TaskData(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID                = Column(Text(length=10000))
    taskSession           = Column(Text(length=10000))
    taskSessionTry        = Column(Text(length=10000))
    trialNum              = Column(Text(length=10000))
    trialTime             = Column(Text(length=10000))
    blockNum              = Column(Text(length=10000))
    trialinBlockNum       = Column(Text(length=10000))
    devaluedBlock         = Column(Text(length=10000))
    fixTime               = Column(Text(length=10000))
    attenIndex            = Column(Text(length=10000))
    attenCheckKey         = Column(Text(length=10000))
    attenCheckTime        = Column(Text(length=10000))
    stimIndex             = Column(Text(length=10000))
    stimTime              = Column(Text(length=10000))
    fbProbTrack           = Column(Text(length=10000))
    randProb              = Column(Text(length=10000))
    responseKey           = Column(Text(length=10000))
    reactionTime          = Column(Text(length=10000))
    playFbSound           = Column(Text(length=10000))
    fbTime                = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_task_session(self):
        return str(self.taskSession)

    def get_task_session_try(self):
        return str(self.taskSessionTry)

    def get_trial_no(self):
        return str(self.trialNum)

    def get_trial_time(self):
        return str(self.trialTime)

    def get_block_no(self):
        return str(self.blockNum)

    def get_trial_in_block_no(self):
        return str(self.trialinBlockNum)

    def get_devalued_block(self):
        return str(self.devaluedBlock)

    def get_fix_time(self):
        return str(self.fixTime)

    def get_atten_index(self):
        return str(self.attenIndex)

    def get_attencheck_key(self):
        return str(self.attenCheckKey)

    def get_attencheck_time(self):
        return str(self.attenCheckTime)

    def get_stim_index(self):
        return str(self.stimIndex)

    def get_stim_time(self):
        return str(self.stimTime)

    def get_fb_prob(self):
        return str(self.fbProbTrack)

    def get_rand_prob(self):
        return str(self.randProb)

    def get_response_key(self):
        return str(self.responseKey)

    def get_reaction_time(self):
        return str(self.reactionTime)

    def get_fb_sound(self):
        return str(self.playFbSound)

    def get_fb_time(self):
        return str(self.fbTime)

    def errors(self):
        errors = super(TaskData, self).errors()
        return errors
