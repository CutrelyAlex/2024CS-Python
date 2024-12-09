import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo

# dish_controller = DishController()
# student_controller = StudentController()

# student = student_controller.find_student_by_name("陈烨烨")[0]

# print(student_controller.get_all_students()[0].name)

# print(dish_controller.find_dish_by_name(student_controller.get_all_students()[0].dining_info_list[0].dishes[0])[0].price)

dishes = DishController()
stu = StudentController().add_student()

print(stu)
