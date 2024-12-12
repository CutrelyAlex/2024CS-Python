from flask import Flask, render_template
from flask_ckeditor import CKEditor
from apps import Dish

app = Flask(__name__) # 项目名称
app.config['WTF_CSRF_ENABLED'] = False # 免除csrf保护
app.register_blueprint(Dish.dish_bp) # 加载菜品蓝图
# app.register_blueprint(Stu.stu_bp)   # 加载学生蓝图
ckeditor = CKEditor(app) # 富文本编辑

'''首页'''
@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)