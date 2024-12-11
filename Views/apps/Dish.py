from flask import Blueprint, render_template, request, jsonify,redirect, flash, url_for
from forms import DishForm
from flask_wtf import CSRFProtect, csrf

from Core.DishController import DishController

'''建立菜品蓝图'''

dish_bp = Blueprint("dish", __name__, url_prefix='/dish')
dishInit = DishController() # 初始化菜品对象

@dish_bp.route('/dish_list', methods=['GET','POST'])
def dish_list():
    f = DishForm()
    if request.method == 'GET':
        dishes = dishInit.get_all_dishes()
        return render_template("MangerDish/index.html", dishes=dishes, form=f)
    if request.method == 'POST':
        name = request.form.get("name")
        if name:
            dishes = dishInit.find_dish_by_name(name) # 根据名字找查菜品
            if not dishes:
                dishes = dishInit.find_dish_by_location(name) # 根据位置找查菜品
        else:
            dishes = dishInit.get_all_dishes()
        return render_template("MangerDish/index.html",
                dishes=dishes, form=f)

'''添加菜品'''
@dish_bp.route('/dish_add', methods=['GET','POST'])
def dish_add():
    f = DishForm()
    if f.validate_on_submit():
        name_list = dishInit.get_all_dish_names()
        if f.name.data in name_list:
            flash("菜名重复，请查询")
            return render_template("MangerDish/add.html", form=f)
        else:
            print(f.validate())
            toListAllergens = f.allergens.data.split() # 将str:allergens --> list:allergens
            dishInit.add_dish(location=f.location.data, name=f.name.data,
            price=f.price.data, category=f.category.data, image_url=f.img_url.data, allergens=toListAllergens,
            description="", calories=f.calories.data)
            return redirect('dish_list')
    return render_template('MangerDish/add.html', form=f)

'''修改菜品'''
@dish_bp.route('/dish_edit/<dish_id>', methods=['GET', 'POST'])
def dish_edit(dish_id):
    if request.method == 'GET':
        dish_obj = dishInit.find_dish_by_name(dish_id)[0] # 根据菜名获得菜品全部信息
        f = DishForm()
        con_allergens = ""  # 将lsit:allergens --> str:allergens
        for show in dish_obj.allergens:
            con_allergens = con_allergens + " " + show 
        f.name.data = dish_obj.name
        f.category.data = dish_obj.category
        f.img_url.data = dish_obj.image_url
        f.calories.data = dish_obj.calories
        f.price.data = dish_obj.price
        f.location.data = dish_obj.location
        f.allergens.data = con_allergens
        return render_template('MangerDish/edit.html', form=f)
    elif request.method == 'POST':
        f = DishForm(request.form)
        dish_obj = dishInit.find_dish_by_name(dish_id)[0]
        dishInit.remove_dish(dish_obj) # 删除原有菜品对象
        if f.is_submitted(): # 检测是否获取了表单,不能通过validate验证？？？
            dish_obj.name = f.name.data
            dish_obj.category = f.category.data
            dish_obj.image_url = f.img_url.data
            dish_obj.calories = f.calories.data
            dish_obj.price = f.price.data
            dish_obj.location = f.location.data
            dish_obj.allergens = f.allergens.data.split()
            return redirect(url_for('dish.dish_list'))
        else:
            return render_template('MangerDish/edit.html', form=f) 

'''删除菜品'''
@dish_bp.route('/dish_del', methods=['GET', 'POST'])
def dish_del():
    remove_dish = request.values.get("dish_id")
    dishInit.remove_dish(remove_dish)
    return jsonify({"code":"200", "message":"删除成功"})
