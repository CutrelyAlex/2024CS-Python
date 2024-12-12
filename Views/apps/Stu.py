from flask import Blueprint, render_template, request, jsonify, redirect, flash
from forms import StuForm
from flask_wtf import CSRFProtect, csrf
from Core.StudentController import StudentController

stu_bp = Blueprint('stu', __name__, url_prefix='/stu')

stuInit = StudentController()

'''学生列表'''
@stu_bp.route('/stu_list', methods=['GET','POST'])
def stu_list():
    students = stuInit.get_all_students()
    if request.method == 'GET':
        return render_template('MangerStu/index.html', students=students)
    elif request.method == 'POST':
        respone = request.form.get('name') # 获取搜索框中的内容
        if respone:
            students = stuInit.find_student_by_name(respone)
            if not students:
                students = stuInit.find_student_by_id(respone)
        else:
            students = stuInit.get_all_students()
        return render_template('MangerStu/index.html', students=students)

'''新增学生'''
@stu_bp.route('/stu_add', methods=['GET', 'POST'])
def stu_add():
    f = StuForm()
    if f.validate_on_submit():
        stu_id = stuInit.find_student_by_id(f.student_id.data)
        if stu_id:
            flash("学号重复，请查询")
            return render_template("MangerStu/add.html", form=f)
        else:
            stuInit.add_student(location=f.student_id.data, name=f.name.data,
            student_id=f.student_id.data, password=f.password.data,profile=int(f.age.data),
            dining_info_list='')
            return redirect('stu_list')
    return render_template('MangerStu/add.html', form=f)


@stu_bp.route("/stu_edit", methods=['GET', 'POST'])
def stu_edit():
    pass

'''删除学生信息'''
@stu_bp.route('/stu_del', methods=['GET','POST'])
def stu_del():
    remove_stu_id = request.values.get("stu_id")
    stuInit.remove_student(remove_stu_id)
    return jsonify({"code":"200", "message":"删除成功"})