from datetime import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.Studentevaluation import *
s = DiningInfo(datetime.now(), dishes=['1','2'], remarks='s',images=['s'])
find = StudentController().add_dining_record("202400301052",dining_info=s)



