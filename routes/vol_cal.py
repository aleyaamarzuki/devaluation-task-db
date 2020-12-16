"""users routes"""
from flask import current_app as app, jsonify, request
from models import VolCal, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/vol_cal/<user_id>', methods=['POST', 'GET'])
def create_vol_cal_data(user_id):
    print(user_id)
    content = request.json
    vol_cal = VolCal()
    vol_cal.userID      = str(content['userID'])
    vol_cal.date        = str(content['date'])
    vol_cal.startTime   = str(content['startTime'])
    vol_cal.volCalStage = str(content['volCalStage'])
    vol_cal.checkTry    = str(content['checkTry'])
    vol_cal.qnTime      = str(content['qnTime'])
    vol_cal.qnRT        = str(content['qnRT'])
    vol_cal.qnNum       = str(content['qnNum'])
    vol_cal.soundIndex  = str(content['soundIndex'])
    vol_cal.soundFocus  = str(content['soundFocus'])
    vol_cal.volume      = str(content['volume'])
    vol_cal.volumePer   = str(content['volumePer'])
    vol_cal.volumeNotLog = str(content['volumeNotLog'])
    vol_cal.playNum     = str(content['playNum'])
    vol_cal.quizAnsIndiv = str(content['quizAnsIndiv'])
    vol_cal.qnPressKey  = str(content['qnPressKey'])
    vol_cal.qnCorrIndiv = str(content['qnCorrIndiv'])
    vol_cal.averRating  = str(content['averRating'])
    vol_cal.arouRating  = str(content['arouRating'])
    vol_cal.averRatingDef= str(content['averRatingDef'])
    vol_cal.arouRatingDef= str(content['arouRatingDef'])
    BaseObject.check_and_save(vol_cal)
    result = dict({"success": "yes"})
    return jsonify(result)
