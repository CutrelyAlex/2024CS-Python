import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo

# dish_controller = DishController()
# student_controller = StudentController()

# student = student_controller.find_student_by_name("陈烨烨")[0]

# print(student_controller.get_all_students()[0].name)

# print(dish_controller.find_dish_by_name(student_controller.get_all_students()[0].dining_info_list[0].dishes[0])[0].price)

dishes = DishController()
stu = StudentController().get_all_students()
for stus in stu:
    print(stus.student_id)
    print(stus.name)
    print(stus.password)
    print(stus.profile.age)
    print(stus.profile.gender)
    print(stus.profile.description)


