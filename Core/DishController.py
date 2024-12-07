import re
from Core.DishModel import *
dish_path = "dishes.json"

class DishController:
    dishes = convert_to_dishes(load_dishes_from_json(dish_path))
    def __init__(self):
        pass
    
    def add_dish(self, location: str, name: str, price: float,
                 category: str, image_url: str, calories: float,
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

