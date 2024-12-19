from Core.DishController import DishController
from flask import Blueprint, render_template, request, jsonify,redirect, flash, url_for
from forms import DishForm
import os

'''
    建立菜品蓝图
    有以下几个主要函数：
        dish_list() 显示菜品列表页面
        dish_add() 添加菜品页面
        dish_edit() 修改菜品页面
        diish_delete 删除菜品页面
'''

dish_bp = Blueprint("dish", __name__, url_prefix='/dish') # 建立菜品蓝图 url: /dish/
dishInit = DishController() # 初始化菜品对象
UPLOAD_FOLDER = 'static\\img'

'''菜品列表'''
@dish_bp.route('/dish_list', methods=['GET','POST'])
def dish_list():
    if request.method == 'GET':
        dishes = dishInit.get_all_dishes()
        return render_template("MangerDish/index.html", dishes=dishes, dishInit=dishInit)
    if request.method == 'POST':
        name = request.form.get("name")
        location = request.form.get("location")
        if name and location != '-1':
            dishes = dishInit.find_dish_by_location(location, name)
        elif name and location == '-1':
            dishes = dishInit.find_dish_by_name(name)
        elif not name and location != '-1':
            dishes = dishInit.get_all_dishes_by_location(location)
        else:
            dishes = dishInit.get_all_dishes()
        return render_template("MangerDish/index.html",
                dishes=dishes)

'''添加菜品'''
@dish_bp.route('/dish_add', methods=['GET','POST'])
def dish_add():
    f = DishForm()
    if f.validate_on_submit():
        img = request.files['img_url']
        if img.filename != '':
            img.save(os.path.join(UPLOAD_FOLDER,img.filename))
        exist_location = []
        names = dishInit.find_dish_by_name(f.name.data) # 查找餐品名
        for name in names:
            exist_location.append(name.location)
        if names and f.location.data in exist_location:
            flash("菜品已存在，请查询")
            return render_template("MangerDish/add.html", form=f)
        else:
            toListAllergens = f.allergens.data.split() # 将str:allergens --> list:allergens
            dishInit.add_dish(location=f.location.data, name=f.name.data,
            price=f.price.data, category=f.category.data, image_url=request.files['img_url'].filename, allergens=toListAllergens,
            description=f.description.data, calories=f.calories.data)
            return redirect('dish_list')
    return render_template('MangerDish/add.html', form=f)

'''修改菜品'''
@dish_bp.route('/dish_edit/<dish_id>', methods=['GET', 'POST'])
def dish_edit(dish_id):
    dish_id = dish_id.strip("()").split(",")
    dish_obj = dishInit.find_dish_by_location(eval(dish_id[1]), eval(dish_id[0]))[0] # 根据菜名获得菜品全部信息
    if request.method == 'GET':
        # print(dish_obj)
        f = DishForm()
        str_allergen = "" # 将allergens列表形式转换成字符串输出
        for allergen in dish_obj.allergens:
            str_allergen += " " + allergen
        str_allergen = str_allergen.strip()
        # f.name.data = dish_obj.name
        f.category.data = dish_obj.category
        f.img_url.data = dish_obj.image_url
        f.calories.data = dish_obj.calories
        f.price.data = dish_obj.price
        # f.location.data = dish_obj.location
        f.allergens.data = str_allergen
        f.description.data = dish_obj.description
        return render_template('MangerDish/edit.html', form=f)
    elif request.method == 'POST':
        f = DishForm(request.form)
        if f.is_submitted(): # 检测是否获取了表单,不能通过validate验证？？？
            # toListAllergens = f.allergens.data.split()
            img = request.files['img_url']
            if img.filename != '':
                img.save(os.path.join(UPLOAD_FOLDER,img.filename))
            toListAllergens = f.allergens.data.split()
            dishInit.update_dish(location=eval(dish_id[1]),name=eval(dish_id[0]), price=f.price.data,
                                 category=f.category.data, image_url=request.files['img_url'].filename, calories=f.calories.data,
                                 allergens=toListAllergens, description=f.description.data)
            return redirect(url_for('dish.dish_list'))
        else:
            return render_template('MangerDish/edit.html', form=f) 

'''删除菜品'''
@dish_bp.route('/dish_del', methods=['GET', 'POST'])
def dish_del():
    remove_dish = eval(request.values.get("dish_id"))
    dishInit.remove_dish(remove_dish[0], remove_dish[1])
    return jsonify({'code':200})