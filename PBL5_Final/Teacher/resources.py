from import_export import resources
from Exam.models import *

class LevelResource(resources.ModelResource):
    class Meta:
        model = Level

class ExamResource(resources.ModelResource):
    class Meta:
        model = Exam

class ExamPartResource(resources.ModelResource):
    class Meta:
        model = ExamPart

class GroupQuestionResource(resources.ModelResource):
    class Meta:
        model = GroupQuestion

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question