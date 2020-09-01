"""users routes"""
from flask import current_app as app, jsonify, request
from models import TaskQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/task_quiz/<user_id>', methods=['POST', 'GET'])
def create_task_quiz(user_id):
    content = request.json
    task_quiz = TaskQuiz()
    task_quiz.userID = str(content['userID'])
    task_quiz.quizTime = str(content['quizTime'])
    task_quiz.taskSession = str(content['taskSession'])
    task_quiz.taskSessionTry = str(content['taskSessionTry'])
    task_quiz.quizQnNum = str(content['quizQnNum'])
    task_quiz.quizQnRT = str(content['quizQnRT'])
    task_quiz.quizContinDefault = str(content['quizContinDefault'])
    task_quiz.quizContin = str(content['quizContin'])
    task_quiz.quizConfDefault = str(content['quizConfDefault'])
    task_quiz.quizConf = str(content['quizConf'])
    BaseObject.check_and_save(task_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
