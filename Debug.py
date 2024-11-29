import datetime  # 新增导入
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.DishModel import Dish
from Core.StudentModel import Student

dish_controller = DishController()
student_controller = StudentController()

student = student_controller.find_student_by_name("陈烨烨")[0]

print(student_controller.get_all_students()[0].name)

d = student_controller.get_all_students()[0].dining_info_list[0].dishes[0]
print(dish_controller.find_dish_by_name(d)[0].price)





