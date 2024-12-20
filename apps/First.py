from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from Core.StudentController import StudentController,DiningInfo
from Core.DishController import DishController
import Core.Statistician as Statistician

'''首页'''
views_bp = Blueprint('views', __name__ ,url_prefix='/views')

def get_dining_time() -> dict:
    '''获取学生就餐时间\n'''
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

@views_bp.route('/index', methods=['GET','POST'])
def index():
    len_stu = len(StudentController().get_all_students()) # 获取学生数量
    len_dish = len(DishController().get_all_dishes()) # 获取菜品数量

    dish_counts = Statistician.Statistician(StudentController()).get_dish_counts(5) # 获取菜品数量
    dish_labels = [labels for labels in dish_counts.keys()] # 菜品名称
    dish_num = [number for number in dish_counts.values()]  # 菜品数量

    time_labels = [labels for labels in get_dining_time().keys()] 
    time_num = [number for number in get_dining_time().values()] 

    return render_template('index.html', len_stu=len_stu, len_dish=len_dish, 
                            labels=dish_labels, datas=dish_num,
                            time_labels=time_labels, time_num=time_num)