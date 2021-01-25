"""users routes"""
from flask import current_app as app, jsonify, request
from models import TaskQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/task_quiz/<user_id>', methods=['POST', 'GET'])
def create_task_quiz(user_id):
    content = request.json
    task_quiz = TaskQuiz()
    task_quiz.userID = str(content['userID'])
    task_quiz.date        = str(content['date'])
    task_quiz.startTime   = str(content['startTime'])
    task_quiz.quizTime = str(content['quizTime'])
    task_quiz.taskSession = str(content['taskSession'])
    task_quiz.taskSessionTry = str(content['taskSessionTry'])
    task_quiz.section = str(content['section'])
    task_quiz.quizQnNum = str(content['quizQnNum'])
    task_quiz.quizQnRT = str(content['quizQnRT'])
    task_quiz.quizStimIndexCount = str(content['quizStimIndexCount'])
    task_quiz.quizStimIndex = str(content['quizStimIndex'])
    task_quiz.quizStimDevalue = str(content['quizStimDevalue'])
    task_quiz.quizStimContin = str(content['quizStimContin'])
    task_quiz.quizContinDefault = str(content['quizContinDefault'])
    task_quiz.quizContin = str(content['quizContin'])
    task_quiz.quizConfDefault = str(content['quizConfDefault'])
    task_quiz.quizConf = str(content['quizConf'])
    task_quiz.quizSoundLabel= str(content['quizSoundLabel'])
    task_quiz.playNum = str(content['playNum'])
    task_quiz.quizVolume = str(content['quizVolume'])
    task_quiz.quizVolumeNotLog = str(content['quizVolumeNotLog'])
    task_quiz.quizAverDefault= str(content['quizAverDefault'])
    task_quiz.quizAver= str(content['quizAver'])

    BaseObject.check_and_save(task_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
