"""users routes"""
from flask import current_app as app, jsonify, request
from models import AttenData, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/atten_data/<user_id>', methods=['POST', 'GET'])
def create_atten_data(user_id):
    print(user_id)
    content = request.json
    atten_data = AttenData()
    atten_data.userID = str(content['userID'])
    atten_data.date        = str(content['date'])
    atten_data.startTime   = str(content['startTime'])
    atten_data.tutorialSession = str(content['tutorialSession'])
    atten_data.tutorialSessionTry = str(content['tutorialSessionTry'])
    atten_data.taskSession = str(content['taskSession'])
    atten_data.taskSessionTry = str(content['taskSessionTry'])
    atten_data.attenTrial = str(content['attenTrial'])
    atten_data.attenTime = str(content['attenTime'])
    atten_data.attenCheckKey = str(content['attenCheckKey'])
    atten_data.attenCheckTime = str(content['attenCheckTime'])
    atten_data.playAttCheck = str(content['playAttCheck'])
    atten_data.volume = str(content['volume'])
    atten_data.volumeNotLog = str(content['volumeNotLog'])
    BaseObject.check_and_save(atten_data)
    result = dict({"success": "yes"})
    return jsonify(result)
