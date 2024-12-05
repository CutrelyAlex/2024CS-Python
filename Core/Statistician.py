from Core.StudentController import *
from Core.DishController import *
from typing import List, Dict

"""
Statistician 模块

提供以下接口:
- __init__(student_controller: StudentController): 初始化统计器
- get_recent_dining_records(n: int) -> List[DiningInfo]: 获取最近的n次就餐记录
- get_dish_counts(n: int) -> Dict[str, int]: 获取最近n次就餐记录中菜品的统计次数
"""

class Statistician:
    def __init__(self, student_controller: StudentController):
        """
        初始化 Statistician 对象

        参数:
            student_controller (StudentController): 学生控制器对象
        """
        self.student_controller = student_controller

    def get_recent_dining_records(self, n: int) -> List[DiningInfo]:
        """
        返回最近n次就餐记录。

        参数:
            n (int): 要获取的记录数量

        返回:
            List[DiningInfo]: 最近的n次就餐记录列表
        """
        dining_records = []
        for student in self.student_controller.get_all_students():
            dining_records.extend(student.dining_info_list)
        dining_records.sort(key=lambda record: record.dining_time, reverse=True)
        return dining_records[:n]

    def get_dish_counts(self, n: int) -> Dict[str, int]:
        """
        根据最近n次就餐记录返回菜品及其出现次数的字典。

        参数:
            n (int): 用于统计的记录数量

        返回:
            Dict[str, int]: 菜品名称及其出现次数的字典
        """
        recent_records = self.get_recent_dining_records(n)
        dish_counts = {}
        for record in recent_records:
            for dish in record.dishes:
                dish_counts[dish] = dish_counts.get(dish, 0) + 1
        return dish_counts

