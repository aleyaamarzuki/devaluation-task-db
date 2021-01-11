"""users routes"""
from flask import current_app as app, jsonify, request
from models import Bonus, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/bonus_data/<user_id>', methods=['POST', 'GET'])
def create_bonus_data(user_id):
    content = request.json
    bonus_data = Bonus()
    bonus_data.userID = str(content['userID'])
    bonus_data.date        = str(content['date'])
    bonus_data.startTime   = str(content['startTime'])
    bonus_data.phase1Contin = str(content['phase1Contin'])
    bonus_data.phase2Contin = str(content['phase2Contin'])
    bonus_data.phase3Contin = str(content['phase3Contin'])
    bonus_data.phase1FbProb = str(content['phase1FbProb'])
    bonus_data.phase2FbProb = str(content['phase2FbProb'])
    bonus_data.phase3FbProb = str(content['phase3FbProb'])
    bonus_data.bonus1 = str(content['bonus1'])
    bonus_data.bonus2 = str(content['bonus2'])
    bonus_data.bonus3 = str(content['bonus3'])
    bonus_data.totalBonus = str(content['totalBonus'])
    BaseObject.check_and_save(bonus_data)
    result = dict({"success": "yes"})
    return jsonify(result)
