# These 2 imports are general for any api
from models.api_errors import ApiErrors
from models.base_object import BaseObject

# These are the custom models to import
from models.TaskData import TaskData
from models.TaskQuiz import TaskQuiz
from models.TutorialData import TutorialData
from models.TutorialQuiz import TutorialQuiz
from models.AttenData import AttenData
from models.Test import Test

__all__ = (
    'ApiErrors',
    'BaseObject',
    'TutorialData',
    'TutorialQuiz',
    'TaskData',
    'TaskQuiz',
    'AttenData',
    'Test',
)
