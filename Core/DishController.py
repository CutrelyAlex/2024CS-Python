"""
DishController 模块

提供以下接口:
- add_dish(location, name, price, category, image_url, calories, allergens, description): 添加菜品
- find_dish_by_name(name): 根据菜名模糊查询菜品
- find_dish(query): 根据菜名或描述模糊查询菜品
- get_all_dishes(): 获取所有菜品
- get_all_dish_names(): 获取所有菜品名称
- remove_dish(name): 根据菜名删除菜品
- find_dish_by_location(location): 根据位置查询菜品
- update_dish(location, name, price=None, category=None, image_url=None, calories=None, allergens=None, description=None): 修改菜品信息
- update_dish_location(name, old_location, new_location): 修改菜品位置
"""

import re
from DishModel import *
dish_path = "dishes.json"

class DishController:
    def __init__(self):
        self.dishes = convert_to_dishes(load_dishes_from_json(dish_path))
    
    def add_dish(self, location: str, name: str, price: float, \
                 category: str, image_url: str, calories: float, \
                 allergens: list, description: str):
        """
        添加菜品接口
        参数: 
            location 位置 str
            name 菜名 str
            price 价格 float
            category 类型 str
            image_url 图片路径 str
            calories 热量 float
            allergens 过敏原 list
            description 描述 str
        无返回
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == location:
                raise ValueError("已经存在此菜品")
        new_dish = Dish(location, name, price, category, image_url, calories, allergens, description)
        self.dishes.append(new_dish)
        save_dishes_to_json(dish_path, self.dishes)
    
    def find_dish_by_name(self, name: str):
        """
        根据菜名模糊查询菜品
        参数:
            name 菜名 str
        返回:
            匹配的菜品对象列表 List[Dish]
        """
        pattern = re.compile(name, re.IGNORECASE)
        matched_dishes = [dish for dish in self.dishes if pattern.search(dish.name)]
        return matched_dishes
    
    def find_dish(self, query: str):
        """
        根据菜名或描述模糊查询菜品
        参数:
            query 查询字符串 str
        返回:
            匹配的菜品对象列表 List[Dish]
        """
        pattern = re.compile(query, re.IGNORECASE)
        matched_dishes = [dish for dish in self.dishes if pattern.search(dish.name) or pattern.search(dish.description)]
        return matched_dishes


    def get_all_dishes(self):
        """
        获取所有菜品
        返回:
            所有菜品对象列表 List[Dish]
        """
        return self.dishes
    
    def get_all_dish_names(self):
        """
        获取所有菜品名称
        返回:
            所有菜品名称列表 List[str]
        """
        return [dish.name for dish in self.dishes]
    
    def remove_dish(self, name: str):
        """
        根据菜名删除菜品
        参数:
            name 菜名 str
        无返回
        """
        self.dishes = [dish for dish in self.dishes if dish.name != name]
        save_dishes_to_json(dish_path, self.dishes)
    
    def find_dish_by_location(self, location: str):
        """
        根据位置查询菜品
        参数:
            location 位置 str
        返回:
            匹配的菜品对象列表 List[Dish]
        """
        matched_dishes = [dish for dish in self.dishes if dish.location == location]
        return matched_dishes

    def update_dish(self, location: str, name: str, price: float = None, \
                    category: str = None, image_url: str = None, calories: float = None, \
                    allergens: list = None, description: str = None):
        """
        修改菜品信息接口
        参数: 
            location 位置 str
            name 菜名 str
            price 价格 float (可选)
            category 类型 str (可选)
            image_url 图片路径 str (可选)
            calories 热量 float (可选)
            allergens 过敏原 list (可选)
            description 描述 str (可选)
        无返回
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == location:
                self._update_dish_attributes(dish, price, category, image_url, calories, allergens, description)
                save_dishes_to_json(dish_path, self.dishes)
                return
        raise ValueError("未找到指定的菜品")

    def update_dish_location(self, name: str, old_location: str, new_location: str):
        """
        修改菜品位置接口
        参数:
            name 菜名 str
            old_location 旧位置 str
            new_location 新位置 str
        无返回
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == old_location:
                dish.location = new_location
                save_dishes_to_json(dish_path, self.dishes)
                return
        raise ValueError("未找到指定的菜品")

    def _update_dish_attributes(self, dish: Dish, price: float = None, \
                                category: str = None, image_url: str = None, calories: float = None, \
                                allergens: list = None, description: str = None):
        """
        更新菜品属性的辅助方法（私有的）
        参数:
            dish 菜品对象 Dish
            price 价格 float (可选)
            category 类型 str (可选)
            image_url 图片路径 str (可选)
            calories 热量 float (可选)
            allergens 过敏原 list (可选)
            description 描述 str (可选)
        无返回
        """
        if price is not None:
            dish.price = price
        if category is not None:
            dish.category = category
        if image_url is not None:
            dish.image_url = image_url
        if calories is not None:
            dish.calories = calories
        if allergens is not None:
            dish.allergens = allergens
        if description is not None:
            dish.description = description