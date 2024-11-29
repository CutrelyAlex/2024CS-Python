"""
DishController 模块

提供以下接口:
- add_dish(location, name, price, category, image_url, calories, allergens, description): 添加菜品
- find_dish_by_name(name): 根据菜名模糊查询菜品
- find_dish(query): 根据菜名或描述模糊查询菜品
- get_all_dishes(): 获取所有菜品
- get_all_dish_names(): 获取所有菜品名称
- remove_dish(name, location): 根据菜名和位置删除菜品
- find_dish_by_location(location): 根据位置查询菜品
- update_dish(location, name, price=None, category=None, image_url=None, calories=None, allergens=None, description=None): 修改菜品信息
- update_dish_location(name, old_location, new_location): 修改菜品位置
- get_dish_price(name, location): 根据菜名和位置获取菜品价格
"""

import re
from Core.DishModel import Dish, convert_to_dishes, load_dishes_from_json, save_dishes_to_json
dish_path = "dishes.json"

class DishController:
    """
    管理菜品的控制器类。

    方法可能返回 `None`，例如在添加已存在的菜品或未找到特定菜品时。
    """
    def __init__(self):
        self.dishes = convert_to_dishes(load_dishes_from_json(dish_path))
    
    def add_dish(self, location: str, name: str, price: float, \
                 category: str, image_url: str, calories: float, \
                 allergens: list, description: str):
        """
        添加菜品接口。

        参数: 
            location (str): 位置
            name (str): 菜名
            price (float): 价格
            category (str): 类型
            image_url (str): 图片路径
            calories (float): 热量
            allergens (list): 过敏原
            description (str): 描述

        返回:
            Dish: 添加的菜品对象
            None 如果菜品已存在
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == location:
                return dish
        new_dish = Dish(location, name, price, category, image_url, calories, allergens, description)
        self.dishes.append(new_dish)
        save_dishes_to_json(dish_path, self.dishes)
    
    def find_dish_by_name(self, name: str):
        """
        根据菜名模糊查询菜品。

        参数:
            name (str): 菜名

        返回:
            List[Dish]: 匹配的菜品对象列表
        """
        pattern = re.compile(name, re.IGNORECASE)
        matched_dishes = [dish for dish in self.dishes if pattern.search(dish.name)]
        return matched_dishes
    
    def find_dish(self, query: str):
        """
        根据菜名或描述模糊查询菜品。

        参数:
            query (str): 查询字符串

        返回:
            List[Dish]: 匹配的菜品对象列表
        """
        pattern = re.compile(query, re.IGNORECASE)
        matched_dishes = [dish for dish in self.dishes if pattern.search(dish.name) or pattern.search(dish.description)]
        return matched_dishes


    def get_all_dishes(self):
        """
        获取所有菜品。

        返回:
            List[Dish]: 所有菜品对象列表
        """
        return self.dishes
    
    def get_all_dish_names(self):
        """
        获取所有菜品名称。

        返回:
            List[str]: 所有菜品名称列表
        """
        return [dish.name for dish in self.dishes]
    
    def remove_dish(self, name: str, location: str):
        """
        根据菜名和位置删除菜品。

        参数:
            name (str): 菜名
            location (str): 位置

        返回:
            None
        """
        self.dishes = [dish for dish in self.dishes if not (dish.name == name and dish.location == location)]
        save_dishes_to_json(dish_path, self.dishes)
    
    def find_dish_by_location(self, location: str):
        """
        根据位置查询菜品。

        参数:
            location (str): 位置

        返回:
            List[Dish]: 匹配的菜品对象列表
        """
        matched_dishes = [dish for dish in self.dishes if dish.location == location]
        return matched_dishes

    def update_dish(self, location: str, name: str, price: float = None, \
                    category: str = None, image_url: str = None, calories: float = None, \
                    allergens: list = None, description: str = None):
        """
        修改菜品信息接口。

        参数: 
            location (str): 位置
            name (str): 菜名
            price (float, optional): 价格
            category (str, optional): 类型
            image_url (str, optional): 图片路径
            calories (float, optional): 热量
            allergens (list, optional): 过敏��
            description (str, optional): 描述

        返回:
            None 如果菜品未找到
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == location:
                self._update_dish_attributes(dish, price, category, image_url, calories, allergens, description)
                save_dishes_to_json(dish_path, self.dishes)
                return
        return None

    def update_dish_location(self, name: str, old_location: str, new_location: str):
        """
        修改菜品位置接口。

        参数:
            name (str): 菜名
            old_location (str): 旧位置
            new_location (str): 新位置

        返回:
            None 如果菜品未找到
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == old_location:
                dish.location = new_location
                save_dishes_to_json(dish_path, self.dishes)
                return
        return None

    def get_dish_price(self, name: str, location: str) -> float:
        """
        根据菜名和位置获取菜品价格。

        参数:
            name (str): 菜名
            location (str): 位置

        返回:
            float: 菜品价格
            None 如果未找到
        """
        for dish in self.dishes:
            if dish.name == name and dish.location == location:
                return dish.price
        return None


    def _update_dish_attributes(self, dish: Dish, price: float = None, \
                                category: str = None, image_url: str = None, calories: float = None, \
                                allergens: list = None, description: str = None):
        """
        更新菜品属性的辅助方法（私有的）。

        参数:
            dish (Dish): 菜品对象
            price (float, optional): 价格
            category (str, optional): 类型
            image_url (str, optional): 图片路径
            calories (float, optional): 热量
            allergens (list, optional): 过敏原
            description (str, optional): 描述

        返回:
            None
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