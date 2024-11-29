from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.DishModel import Dish
from Core.StudentModel import Student

dish_controller = DishController()
student_controller = StudentController()

print(student_controller.get_all_students()[0].name)

print(student_controller.get_all_students()[0].dining_info_list[0].dishes[0])

