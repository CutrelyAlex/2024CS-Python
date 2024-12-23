from flask import Flask, redirect, url_for
from apps import Dish, Stu, Dining_info, First
import time

start = time.perf_counter()
app = Flask(__name__) # 项目名称
app.secret_key = "dasswdadsd13213" # csrf保护
app.register_blueprint(First.views_bp) # 加载首页蓝图
app.register_blueprint(Dish.dish_bp) # 加载菜品蓝图
app.register_blueprint(Stu.stu_bp)   # 加载学生蓝图
app.register_blueprint(Dining_info.dining_bp) # 加载就餐记录蓝图

'''首页'''
@app.route('/')
def index():
    return redirect(url_for("views.index"))

if __name__ == '__main__':
    end = time.perf_counter()
    print("程序运行时间：", round(end-start, 2),"s")
    app.run()
    