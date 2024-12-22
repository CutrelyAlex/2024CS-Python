from datetime import datetime
from Core.DishController import DishController
from Core.StudentController import StudentController, DiningInfo
import Core.Statistician as Statistician
# s = DiningInfo(datetime.now(), dishes=['1','2'], remarks='s',images=['s'])
# find = StudentController().add_dining_record("202400301052",dining_info=s)
import pandas as pd

file_path = '工1.xlsx'
df = pd.read_excel(file_path)

# print("Execl文件中的数据为：")、
df.fillna("未知", inplace=True)
s = df.values.tolist()
dishInit = DishController()

for i in s:
    location = i[0]
    name = i[1]
    price = i[2]
    calories = i[3]
    # allergens = i[4]
    # print(allergens, type(allergens))
    # images = i[5]
    # description = i[6]
    print()
    if location == '北区饭堂':
        location = '北区'
    elif location == '南堕':
        location = '南堕落街'
    dishInit.add_dish(location=location, name=name, category='主菜',
                      price=price, calories=float(calories[:len(calories)-1]), 
                      allergens="无", image_url="无", description="无")