import json

class Dish:
    '''菜品模型'''
    def __init__(self, name: str, price: float, category: str, image_url: str, calories: float, allergens: list, description: str):
        self.name = name
        self.price = price
        self.category = category
        self.image_url = image_url
        self.calories = calories
        self.allergens = allergens
        self.description = description

    def display_info(self):
        return f"菜品名称: {self.name}\n价格: {self.price}元\n分类: {self.category}\n热量: {self.calories}卡\n过敏源: {', '.join(self.allergens)}\n描述: {self.description}"



def load_dishes_from_json(file_path: str):
    """
    从 JSON 文件加载菜品数据
    参数:
        file_path 文件路径(json文件) str
    返回：
        菜品Json数据列表 List
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        dishes_data = json.load(file)
        return dishes_data



def convert_to_dishes(dishes_data):
    '''
    转换 JSON 数据为菜品对象
    参数:
        dishes_data 菜品Json数据列表
    返回:
        菜品对象列表 List
    '''
    dishes = []
    for data in dishes_data:
        dish = Dish(
            name=data['name'],
            price=data['price'],
            category=data['category'],
            image_url=data['image_url'],
            calories=data['calories'],
            allergens=data['allergens'],
            description=data['description']
        )
        dishes.append(dish)
    return dishes


def save_dishes_to_json(file_path: str, dishes):
    """
    将菜品数据保存到 JSON 文件
    参数: 
        file_path 文件路径 str
        dishes 菜品列表 list
    无返回
    """
    dishes_data = [dish.__dict__ for dish in dishes]  # 将菜品对象转换为字典
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dishes_data, file, ensure_ascii=False, indent=4)  # 保存为 JSON 格式