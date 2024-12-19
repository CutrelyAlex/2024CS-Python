from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from forms import StuForm
from Core.StudentController import StudentController, DiningInfo
import os
from werkzeug.utils import secure_filename

'''
    学生管理蓝图
    有以下几个主要函数：
        -allowed_file() 判断图片格式是否正确
        -stu_list() 显示学生列表页面
        -stu_add() 添加学生页面
        -stu_upload() 上传图片
        -stu_delete() 删除图片
        -stu_uploaded() 保存图片
        -stu_edit() 修改学生页面
        -stu_del() 删除学生页面
'''

UPLOAD_FOLDER = 'static\\img' # 图片上传路径
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} # 允许上传的图片格式
SAVE_FOLDER_List = [] # 保存图片的路径列表
stu_bp = Blueprint('stu', __name__, url_prefix='/stu') # 建立学生蓝图 url: /stu/
stuInit = StudentController() # 初始化学生对象

'''判断图片格式是否正确'''
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

'''上传图片'''
@stu_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

'''保存图片'''
@stu_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '没有图片'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择图片'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        file_url = url_for('stu.uploaded_file', filename=filename)
        SAVE_FOLDER_List.append(file_path)
        # print(SAVE_FOLDER_List)
        return jsonify({'success': '图片上传成功', 'url': file_url, 'filename': filename}), 200
    return jsonify({'error': '图片上传失败'}), 400

'''删除图片'''
@stu_bp.route('/delete_file', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')
    if filename and allowed_file(filename):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            SAVE_FOLDER_List.remove(file_path)
            # print(SAVE_FOLDER_List)
            return jsonify({'success': '删除成功'}), 200
    return jsonify({'error': '删除失败'}), 400

'''新增学生'''
@stu_bp.route('/stu_add', methods=['GET', 'POST'])
def stu_add():
    f = StuForm()
    if f.is_submitted():
        stu_id = stuInit.find_student_by_id(f.student_id.data)
        if stu_id:
            flash("学号重复，请查询") 
            return render_template("MangerStu/add.html", form=f)
        elif f.gender.data == "-1":
            flash("性别不能为空")
            return render_template("MangerStu/add_html", form=f)
        else:
            dining_record = DiningInfo(dining_time=f.datetime.data, dishes=f.dishes.data,
            remarks=f.remarks.data, images=SAVE_FOLDER_List)
            stuInit.add_student(name=f.name.data,
            student_id=f.student_id.data, password=f.password.data,
            profile={"age":f.age.data,"gender":f.gender.data,"description":f.description.data},
            dining_info_list=[dining_record])
            # stuInit.add_dining_record(student_id=f.student_id.data, dining_info=dining_record)
            return redirect('stu_list')
    return render_template('MangerStu/add.html', form=f)

'''修改学生信息'''
@stu_bp.route("/stu_edit/<stu_id>", methods=['GET', 'POST'])
def stu_edit(stu_id):
    if request.method == 'GET':
        stu_obj = stuInit.find_student_by_id(stu_id)
        f = StuForm()
        f.student_id.data = stu_obj.student_id
        f.name.data = stu_obj.name
        f.password.data = stu_obj.password
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
@stu_bp.route('/stu_del/<stu_id>', methods=['GET','POST'])
def stu_del(stu_id):
    stuInit.remove_student(stu_id)
    return redirect(url_for('stu.stu_list'))