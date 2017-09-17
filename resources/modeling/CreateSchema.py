from sqlalchemy import create_engine

from resources.modeling import AbstractModel, UserModel

engine = create_engine('postgresql+psycopg2://pguser:p@localhost/quizdb', echo=True)
connection = engine.connect()



# abstract = AbstractModel.AbstractModel(engine)
UserModel.UserModel()
# ExamModel(engine).create()
# ExamQuestionModel(engine).create()
# ExamModuleModel(engine).create()
# ModuleCategoryModel(engine).create()
# Question(engine).create()
# AnswerModel(engine).create()
# ExplanationModel(engine).create()



