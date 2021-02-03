"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TaskQuiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                = Column(Text(length=10000))
    startTime           = Column(Text(length=10000))
    quizTime             = Column(Text(length=10000))
    taskSession          = Column(Text(length=10000))
    taskSessionTry       = Column(Text(length=10000))
    section             = Column(Text(length=10000))
    quizQnNum            = Column(Text(length=10000))
    quizQnRT             = Column(Text(length=10000))
    quizStimIndexCount   = Column(Text(length=10000))
    quizStimIndex        = Column(Text(length=10000))
    quizStimContin       = Column(Text(length=10000))
    quizStimDevalue      = Column(Text(length=10000))
    quizContinDefault    = Column(Text(length=10000))
    quizContin           = Column(Text(length=10000))
    quizConfDefault      = Column(Text(length=10000))
    quizConf             = Column(Text(length=10000))
    quizSoundLabel       = Column(Text(length=10000))
    playNum              = Column(Text(length=10000))
    quizVolume           = Column(Text(length=10000))
    quizVolumeNotLog     = Column(Text(length=10000))
    quizAverDefault      = Column(Text(length=10000))
    quizAver             = Column(Text(length=10000))
    checkPoint           = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_startTime(self):
        return str(self.startTime)

    def get_trial_time(self):
        return str(self.quizTime)

    def get_task_session(self):
        return str(self.taskSession)

    def get_task_session_try(self):
        return str(self.taskSessionTry)

    def get_quiz_section(self):
        return str(self.section)

    def get_quiz_question_no(self):
        return str(self.quizQnNum)

    def get_quiz_rt(self):
        return str(self.quizQnRT)

    def get_stim_index_count(self):
        return str(self.quizStimIndexCount)

    def get_stim_index(self):
        return str(self.quizStimIndex)

    def get_stim_contin(self):
        return str(self.quizStimContin)

    def get_stim_devalue(self):
        return str(self.quizStimDevalue)

    def get_contin_def(self):
        return str(self.quizContinDefault)

    def get_contin(self):
        return str(self.quizContin)

    def get_conf_def(self):
        return str(self.quizConfDefault)

    def get_conf(self):
        return str(self.quizConf)

    def get_sound_label(self):
        return str(self.quizSoundLabel)

    def get_playNum(self):
        return str(self.playNum)

    def get_quizVolume(self):
        return str(self.quizVolume)

    def get_quizVolumeNotLog(self):
        return str(self.quizVolumeNotLog)

    def get_sound_aver_def(self):
        return str(self.quizAverDefault)

    def get_sound_aver(self):
        return str(self.quizAver)

    def get_checkPoint(self):
        return str(self.checkPoint)

    def errors(self):
        errors = super(TaskQuiz, self).errors()
        return errors
