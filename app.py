from flask import Flask, render_template
from apps import Dish, Stu

app = Flask(__name__) # 项目名称
app.secret_key = "dasswdadsd13213" # 免除csrf保护
app.register_blueprint(Dish.dish_bp) # 加载菜品蓝图
app.register_blueprint(Stu.stu_bp)   # 加载学生蓝图

'''首页'''
@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()