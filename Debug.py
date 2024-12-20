from datetime import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.Studentevaluation import *
# s = DiningInfo(datetime.now(), dishes=['1','2'], remarks='s',images=['s'])
# find = StudentController().add_dining_record("202400301052",dining_info=s)

s1 = StudentController().get_all_students()
# stu_id_list = []
# for stu in s1:
#     stu_id_list.append(stu.student_id)
# print(stu_id_list)
# s = StudentController().find_student_by_id("202400301052")
# print(s.dining_info_list[0].dining_time)
print(s1[0].dining_info_list)


