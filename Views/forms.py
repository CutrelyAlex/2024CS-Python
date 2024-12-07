from wtforms import StringField, TextAreaField, SelectField, FileField, FloatField, SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.validators import Length, DataRequired

class DishForm(FlaskForm):
    name = StringField(label="菜的名称", validators=[
        DataRequired(message="菜名不能为空"),
        Length(min=0, max=30,message="菜名不能超过30个字")
    ], render_kw={"class":"form-control", "placeholder":"请输入菜名"})

    category = StringField(label="菜的种类", validators=[
        DataRequired(message="种类不能为空"),
    ], render_kw={"class":"form-control", "placeholder":"请输入种类"})

    img_url = FileField(label="菜品图片",
    validators=[FileAllowed(upload_set=['png','jpg'],message="只能上传图片格式")])
    
    calories = FloatField(label="热量",
            validators=[DataRequired(message="热量不能为空"),],
            render_kw={"class":"form-control", "placeholder":"请输入热量"})
    
    price = FloatField(label="菜的价格",
            validators=[DataRequired(message="价格不能为空"),],
            render_kw={"class":"form-control", "placeholder":"请输入价格"})

    location = SelectField(label="菜的位置",
    choices=[('北区',"北区"), ('南区','南区')], 
    render_kw={"class":"form-control custom-select", "placeholder":"请选择位置"})
    
    allergens = TextAreaField(label="菜的原材料", validators=[
        DataRequired(message="材料不能为空"),
    ], render_kw={"class":"form-control", "placeholder":"请输入材料", "rows":5, "cols":50})
