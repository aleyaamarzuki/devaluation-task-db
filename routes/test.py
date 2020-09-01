"""users routes"""
from flask import current_app as app, jsonify, request
from models import Test, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/test/<user_id>', methods=['POST', 'GET'])
def create_test(user_id):
    content = request.json()
    test = Test()
    # print(content)
    # print(test)
    # print(test.userID)
    # print(str(content['userID']))
    test.userID = str(content['userID'])
    BaseObject.check_and_save(test)
    result = dict({"success": "yes"})
    print(result)
    return jsonify(result)
