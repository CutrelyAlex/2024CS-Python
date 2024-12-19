from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from forms import StuForm
from Core.StudentController import StudentController, DiningInfo

stu_bp = Blueprint('stu', __name__, url_prefix='/stu')

stuInit = StudentController()

'''学生列表'''
@stu_bp.route('/stu_list', methods=['GET','POST'])
def stu_list():
    if request.method == 'GET':
        studetns = stuInit.get_all_students()
        return render_template('MangerStu/index.html', students=studetns)
    elif request.method == 'POST':
        find = request.form.get("IdorName")
        if find:
            students = [stuInit.find_student_by_id(find)]
            if students == [None]:
                students = stuInit.find_student_by_name(find)
        else:
            students = stuInit.get_all_students()
        return render_template("MangerStu/index.html", students=students)   
        

'''新增学生'''
@stu_bp.route('/stu_add', methods=['GET', 'POST'])
def stu_add():
    f = StuForm()
    if f.validate_on_submit():
        stu_id = stuInit.find_student_by_id(f.student_id.data)
        if stu_id:
            flash("学号重复，请查询") 
            return render_template("MangerStu/add.html", form=f)
        elif f.gender.data == "-1":
            flash("性别不能为空")
            return render_template("MangerStu/add_html", form=f)
        else:
            stuInit.add_student(location=f.student_id.data, name=f.name.data,
            student_id=f.student_id.data, password=f.password.data,profile=int(f.age.data),
            dining_info_list='')
            return redirect('stu_list')
    return render_template('MangerStu/add.html', form=f)


@stu_bp.route("/stu_edit/<stu_id>", methods=['GET', 'POST'])
def stu_edit(stu_id):
    if request.method == 'GET':
        stu_obj = stuInit.find_student_by_id(stu_id)
        f = StuForm()
        f.student_id.data = stu_obj.student_id
        f.name.data = stu_obj.name
        f.password.data = stu_obj.password
        # print(f.age.data, stu_obj, stu_obj.profile.age)
        try:
            f.age.data = stu_obj.profile.age
            f.gender.data = stu_obj.profile.gender
            f.description.data = stu_obj.profile.description
        except AttributeError:
            f.age.data = stu_obj.profile['age']
            f.gender.data = stu_obj.profile['gender']
            f.description.data = stu_obj.profile['description']

        return render_template('MangerStu/edit.html', form=f, s_id=stu_obj.student_id)
    elif request.method == 'POST':
        stu_obj = stuInit.find_student_by_id(stu_id)
        f = StuForm(request.form)
        if f.is_submitted():
            try:
                stuInit.update_student(student_id=stu_obj.student_id,
                name=f.name.data, password=f.password.data, 
                profile={"age":f.age.data, "gender":f.gender.data, "description":f.description.data})
            except AttributeError:
                return "还在开发中......."
            return redirect(url_for('stu.stu_list'))
        else:
            return render_template('MangerStu/edit.html', form=f, s_id=stu_obj.student_id)

'''删除学生信息'''
@stu_bp.route('/stu_del', methods=['GET','POST'])
def stu_del():
    remove_stu_id = request.values.get("stu_id")
    stuInit.remove_student(remove_stu_id)
    return jsonify({"code":"200", "message":"删除成功"})