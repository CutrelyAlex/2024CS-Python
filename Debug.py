from datetime import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.Studentevaluation import *
import Core.Statistician as Statistician
# s = DiningInfo(datetime.now(), dishes=['1','2'], remarks='s',images=['s'])
# find = StudentController().add_dining_record("202400301052",dining_info=s)

s = StudentController().get_all_students()[0]
print(s.dining_info_list[0].dining_time.hour)

def get_dining_time() -> dict:
    time = {'早餐':0,'午餐':0,'晚餐':0}
    for students in StudentController().get_all_students():
        for dining in students.dining_info_list:
            if 7<=dining.dining_time.hour<9:
                time['早餐'] = time.get('早餐',0) + 1
            elif 12<=dining.dining_time.hour<14:
                time['午餐'] = time.get('午餐',0) + 1
            elif 17<=dining.dining_time.hour<19:
                time['晚餐'] = time.get('晚餐',0) + 1
            else:
                pass
    sort_time = sorted(time.items(),key=lambda x:x[1],reverse=True)
    return dict(sort_time)

print(get_dining_time())


