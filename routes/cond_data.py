"""users routes"""
from flask import current_app as app, jsonify, request
from models import CondData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/cond_data/<user_id>', methods=['POST', 'GET'])
def create_cond_data(user_id):
    content = request.json
    cond_data = CondData()
    cond_data.userID = str(content['userID'])
    cond_data.date        = str(content['date'])
    cond_data.startTime   = str(content['startTime'])
    cond_data.restartTime   = str(content['restartTime'])
    cond_data.session   = str(content['session'])
    cond_data.stimCondTrack   = str(content['stimCondTrack'])
    cond_data.totalTrialLog1 = str(content['totalTrialLog1'])
    cond_data.totalTrialLog2 = str(content['totalTrialLog2'])
    cond_data.totalTrialLog3 = str(content['totalTrialLog3'])
    cond_data.trialPerBlockNumLog1 = str(content['trialPerBlockNumLog1'])
    cond_data.trialPerBlockNumLog2 = str(content['trialPerBlockNumLog2'])
    cond_data.trialPerBlockNumLog3 = str(content['trialPerBlockNumLog3'])
    cond_data.stimIndexLog1 = str(content['stimIndexLog1'])
    cond_data.stimIndexLog2 = str(content['stimIndexLog2'])
    cond_data.stimIndexLog3 = str(content['stimIndexLog3'])
    cond_data.attenIndexLog1 = str(content['attenIndexLog1'])
    cond_data.attenIndexLog2 = str(content['attenIndexLog2'])
    cond_data.attenIndexLog3 = str(content['attenIndexLog3'])
    cond_data.totalBlockLog1 = str(content['totalBlockLog1'])
    cond_data.totalBlockLog2 = str(content['totalBlockLog2'])
    cond_data.totalBlockLog3 = str(content['totalBlockLog3'])
    cond_data.attenCheckAllLog1 = str(content['attenCheckAllLog1'])
    cond_data.attenCheckAllLog2 = str(content['attenCheckAllLog2'])
    cond_data.attenCheckAllLog3 = str(content['attenCheckAllLog3'])
    cond_data.outcomeLog1 = str(content['outcomeLog1'])
    cond_data.outcomeLog2 = str(content['outcomeLog2'])
    cond_data.outcomeLog3 = str(content['outcomeLog3'])

    BaseObject.check_and_save(cond_data)
    result = dict({"success": "yes"})
    return jsonify(result)
