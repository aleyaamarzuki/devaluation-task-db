"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class PsychQuiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID           = Column(Text(length=10000))
    date             = Column(Text(length=10000))
    startTime        = Column(Text(length=10000))
    qnTimeStart      = Column(Text(length=10000))
    qnTimeEnd        = Column(Text(length=10000))
    PgFinish_demo    = Column(Text(length=10000))
    PgFinish_OCIR    = Column(Text(length=10000))

    PgFinish_STAI_Y2  = Column(Text(length=10000))
    PgFinish_BIS11    = Column(Text(length=10000))
    PgFinish_SDS      = Column(Text(length=10000))
    PgFinish_ASI3   = Column(Text(length=10000))
    PgFinish_BEAQ   = Column(Text(length=10000))

    PgFinish_WHOQOL_1   = Column(Text(length=10000))
    PgFinish_WHOQOL_2   = Column(Text(length=10000))
    PgFinish_WHOQOL_3   = Column(Text(length=10000))
    PgFinish_WHOQOL_4   = Column(Text(length=10000))
    PgFinish_WHOQOL_5   = Column(Text(length=10000))
    PgFinish_WHOQOL_6   = Column(Text(length=10000))
    PgFinish_WHOQOL_7   = Column(Text(length=10000))
    PgFinish_WHOQOL_8   = Column(Text(length=10000))

    PgFinish_IQ_text    = Column(Text(length=10000))
    PgFinish_IQ_image      = Column(Text(length=10000))

    PgRT_demo        = Column(Text(length=10000))
    PgRT_OCIR        = Column(Text(length=10000))

    PgRT_STAI_Y2     = Column(Text(length=10000))
    PgRT_BIS11       = Column(Text(length=10000))
    PgRT_SDS         = Column(Text(length=10000))
    PgRT_ASI3       = Column(Text(length=10000))
    PgRT_BEAQ      = Column(Text(length=10000))

    PgRT_WHOQOL_1   = Column(Text(length=10000))
    PgRT_WHOQOL_2   = Column(Text(length=10000))
    PgRT_WHOQOL_3   = Column(Text(length=10000))
    PgRT_WHOQOL_4   = Column(Text(length=10000))
    PgRT_WHOQOL_5   = Column(Text(length=10000))
    PgRT_WHOQOL_6   = Column(Text(length=10000))
    PgRT_WHOQOL_7   = Column(Text(length=10000))
    PgRT_WHOQOL_8   = Column(Text(length=10000))


    PgRT_IQ_text       = Column(Text(length=10000))
    PgRT_IQ_image        = Column(Text(length=10000))
    age              = Column(Text(length=10000))
    gender           = Column(Text(length=10000))
    OCIR             = Column(Text(length=10000))
    STAI_Y2          = Column(Text(length=10000))
    BIS11            = Column(Text(length=10000))
    SDS              = Column(Text(length=10000))
    ASI3              = Column(Text(length=10000))

    BEAQ              = Column(Text(length=10000))

    WHOQOL_1   = Column(Text(length=10000))
    WHOQOL_2   = Column(Text(length=10000))
    WHOQOL_3   = Column(Text(length=10000))
    WHOQOL_4   = Column(Text(length=10000))
    WHOQOL_5   = Column(Text(length=10000))
    WHOQOL_6   = Column(Text(length=10000))
    WHOQOL_7   = Column(Text(length=10000))
    WHOQOL_8   = Column(Text(length=10000))

    IQ_1              = Column(Text(length=10000))
    IQ_2              = Column(Text(length=10000))
    IQ_3              = Column(Text(length=10000))
    IQ_4              = Column(Text(length=10000))
    IQ_5              = Column(Text(length=10000))
    IQ_6              = Column(Text(length=10000))
    IQ_7              = Column(Text(length=10000))
    IQ_8              = Column(Text(length=10000))
    IQimage_1              = Column(Text(length=10000))
    IQimage_2              = Column(Text(length=10000))
    IQimage_3              = Column(Text(length=10000))
    IQimage_4              = Column(Text(length=10000))
    IQimage_5              = Column(Text(length=10000))
    IQimage_6              = Column(Text(length=10000))
    IQimage_7              = Column(Text(length=10000))
    IQimage_8              = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_start_time(self):
        return str(self.startTime)

    def get_qn_start(self):
        return str(self.qnTimeStart)

    def get_qn_end(self):
        return str(self.qnTimeEnd)

    def get_pg0_finish(self):
        return str(self.PgFinish_demo)

    def get_pg1_finish(self):
        return str(self.PgFinish_OCIR)

    def get_pg3_finish(self):
        return str(self.PgFinish_STAI_Y2)

    def get_pg4_finish(self):
        return str(self.PgFinish_BIS11)

    def get_pg5_finish(self):
        return str(self.PgFinish_SDS)

    def get_pg7_finish(self):
        return str(self.PgFinish_ASI3)

    def get_pg8_finish(self):
        return str(self.PgFinish_BEAQ)

    def get_pg11_finish(self):
        return str(self.PgFinish_WHOQOL_1)

    def get_pg12_finish(self):
        return str(self.PgFinish_WHOQOL_2)

    def get_pg13_finish(self):
        return str(self.PgFinish_WHOQOL_3)

    def get_pg14_finish(self):
        return str(self.PgFinish_WHOQOL_4)

    def get_pg15_finish(self):
        return str(self.PgFinish_WHOQOL_5)

    def get_pg16_finish(self):
        return str(self.PgFinish_WHOQOL_6)

    def get_pg17_finish(self):
        return str(self.PgFinish_WHOQOL_7)

    def get_pg18_finish(self):
        return str(self.PgFinish_WHOQOL_8)

    def get_pg9_finish(self):
        return str(self.PgFinish_IQ_text)

    def get_pg10_finish(self):
        return str(self.PgFinish_IQ_image)

    def get_pg0_rt(self):
        return str(self.PgRT_demo)

    def get_pg1_rt(self):
        return str(self.PgRT_OCIR)

    def get_pg3_rt(self):
        return str(self.PgRT_STAI_Y2)

    def get_pg4_rt(self):
        return str(self.PgRT_BIS11)

    def get_pg5_rt(self):
        return str(self.PgRT_SDS)

    def get_pg7_rt(self):
        return str(self.PgRT_ASI3)

    def get_pg8_rt(self):
        return str(self.PgRT_BEAQ)

     def get_pg11_rt(self):
        return str(self.PgRT_WHOQOL_1)

    def get_pg12_rt(self):
        return str(self.PgRT_WHOQOL_2)

    def get_pg13_rt(self):
        return str(self.PgRT_WHOQOL_3)

    def get_pg14_rt(self):
        return str(self.PgRT_WHOQOL_4)

    def get_pg15_rt(self):
        return str(self.PgRT_WHOQOL_5)

    def get_pg16_rt(self):
        return str(self.PgRT_WHOQOL_6)

    def get_pg17_rt(self):
        return str(self.PgRT_WHOQOL_7)

    def get_pg18_rt(self):
        return str(self.PgRT_WHOQOL_8)

    def get_pg9_rt(self):
        return str(self.PgRT_IQ_text)

    def get_pg10_rt(self):
        return str(self.PgRT_IQ_image)

    def get_age(self):
        return str(self.age)

    def get_gender(self):
        return str(self.gender)

    def get_ocir(self):
        return str(self.OCIR)

    def get_staiTwo(self):
        return str(self.STAI_Y2)

    def get_bis(self):
        return str(self.BIS11)

    def get_sds(self):
        return str(self.SDS)

    def get_asi(self):
        return str(self.ASI3)

    def get_beaq(self):
        return str(self.BEAQ)

     def get_pg11_whoqol_1(self):
        return str(self.WHOQOL_1)

    def get_pg12_whoqol_2(self):
        return str(self.WHOQOL_2)

    def get_pg13_whoqol_3(self):
        return str(self.WHOQOL_3)

    def get_pg14_whoqol_4(self):
        return str(self.WHOQOL_4)

    def get_pg15_whoqol_5(self):
        return str(self.WHOQOL_5)

    def get_pg16_whoqol_6(self):
        return str(self.WHOQOL_6)

    def get_pg17_whoqol_7(self):
        return str(self.WHOQOL_7)

    def get_pg18_whoqol_8(self):
        return str(self.WHOQOL_8)


    def get_iq1(self):
        return str(self.IQ_1)

    def get_iq3(self):
        return str(self.IQ_3)

    def get_iq4(self):
        return str(self.IQ_4)

    def get_iq5(self):
        return str(self.IQ_5)

    def get_iq6(self):
        return str(self.IQ_6)

    def get_iq7(self):
        return str(self.IQ_7)

    def get_iq8(self):
        return str(self.IQ_8)

    def get_iqimage1(self):
        return str(self.IQimage_1)

    def get_iqimage3(self):
        return str(self.IQimage_3)

    def get_iqimage4(self):
        return str(self.IQimage_4)

    def get_iqimage5(self):
        return str(self.IQimage_5)

    def get_iqimage6(self):
        return str(self.IQimage_6)

    def get_iqimage7(self):
        return str(self.IQimage_7)

    def get_iqimage8(self):
        return str(self.IQimage_8)

    def errors(self):
        errors = super(PsychQuiz, self).errors()
        return errors
