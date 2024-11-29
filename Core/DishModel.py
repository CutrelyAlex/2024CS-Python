import json
from typing import List, Dict, Any

class Dish:
    '''菜品模型'''
    def __init__(self, location: str, name: str, price: float, category: str, image_url: str, calories: float, \
                 allergens: List[str], description: str):
        '''
        初始化 Dish 对象
        参数:
            location: 菜品位置 str
            name: 菜品名称 str
            price: 菜品价格 float
            category: 菜品分类 str
            image_url: 菜品图片 URL str
            calories: 菜品热量 float
            allergens: 过敏源列表 List[str]
            description: 菜品描述 str
        '''
        self.location = location
        self.name = name
        self.price = price
        self.category = category
        self.image_url = image_url
        self.calories = calories
        self.allergens = allergens
        self.description = description
        self.validate()

    def validate(self):
        '''验证菜品数据的有效性'''
        if not self.name:
            raise ValueError("菜品名称不能为空")
        if self.price < 0:
            raise ValueError("菜品价格不能为负数")
        if self.calories < 0:
            raise ValueError("菜品热量不能为负数")


    def __str__(self) -> str:
        '''返回菜品的字符串表示'''
        return f"{self.name} ({self.category}) - {self.price}元"

    def __eq__(self, other) -> bool:
        '''比较两个菜品对象是否相等'''
        if isinstance(other, Dish):
            return self.name == other.name and self.location == other.location
        return False

def load_dishes_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    从 JSON 文件加载菜品数据
    参数:
        file_path 文件路径(json文件) str
    返回：
        菜品Json数据列表 List[Dict[str, Any]]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            dishes_data = json.load(file)
            return dishes_data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"加载 JSON 文件时出错: {e}")
        return []

def convert_to_dishes(dishes_data: List[Dict[str, Any]]) -> List[Dish]:
    '''
    转换 JSON 数据为菜品对象
    参数:
        dishes_data 菜品Json数据列表 List[Dict[str, Any]]
    返回:
        菜品对象列表 List[Dish]
    '''
    dishes = []
    for data in dishes_data:
        try:
            dish = Dish(
                location=data["location"],
                name=data['name'],
                price=data['price'],
                category=data['category'],
                image_url=data['image_url'],
                calories=data['calories'],
                allergens=data['allergens'],
                description=data['description']
            )
            dishes.append(dish)
        except KeyError as e:
            print(f"数据中缺少键: {e}")
    return dishes

def save_dishes_to_json(file_path: str, dishes: List[Dish]) -> None:
    """
    将菜品数据保存到 JSON 文件
    参数: 
        file_path 文件路径 str
        dishes 菜品列表 List[Dish]
    无返回
    """
    dishes_data = [dish.__dict__ for dish in dishes]  # 将菜品对象转换为字典
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dishes_data, file, ensure_ascii=False, indent=4)  # 保存为 JSON 格式
    except IOError as e:
        print(f"保存 JSON 文件时出错: {e}")