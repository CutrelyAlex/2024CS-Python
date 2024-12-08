import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
from Core.StudentEvaluation import *

loaded_evaluations = convert_to_evaluations(load_evaluations_from_json('evaluations.json'))
new_evaluation = Evaluation(
    date=datetime.now(),
    dish='意大利吧',
    student_id='202600331192',
    content='大便啊'
)
loaded_evaluations.append(new_evaluation)
print("添加新的评价:")

# Save evaluations to JSON
save_evaluations_to_json('evaluations.json', loaded_evaluations)        
print("保存评价到JSON文件")

# Load evaluations from JSON
loaded_evaluations = load_evaluations_from_json('evaluations.json')
print("Loaded evaluations:")
for eval in loaded_evaluations:
    print(eval)







