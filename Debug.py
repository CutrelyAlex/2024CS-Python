from datetime import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.Studentevaluation import *

s = [StudentController().find_student_by_id("202400301052")]
print(s[0].profile.age)

