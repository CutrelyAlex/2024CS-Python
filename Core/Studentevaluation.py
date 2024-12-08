import json
from typing import List, Dict, Any
from datetime import datetime

from Core.DishModel import Dish


# 评价信息类
class Evaluation:
    """
    评价类，用于表示学生对菜品的评价信息
    """
    def __init__(self, date: datetime, dish: str, student_id: str, content: str):
        """
        初始化Evaluation对象
        参数:
            date: 评价日期 datetime
            dish: 对应菜品名称 str
            student_id: 评价人学号 str
            content: 评价内容 str
        """
        self.date = date
        self.dish = dish
        self.student_id = student_id
        self.content = content

    def __str__(self) -> str:
        """
        返回评价的字符串表示形式
        """
        return f"评价人学号: {self.student_id}，菜品: {self.dish}，评价内容: {self.content}，评价日期: {self.date}"

    def to_dict(self) -> Dict[str, Any]:
        """
        将评价对象转换为字典，方便后续进行JSON序列化操作
        """
        return {
            "date": self.date.isoformat(),
            "dish": self.dish,
            "student_id": self.student_id,
            "content": self.content
        }


# 从JSON文件加载评价数据
def load_evaluations_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    从JSON文件加载评价数据
    参数:
        file_path 文件路径(json文件) str
    返回：
        评价数据的字典列表 List[Dict[str, Any]]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            evaluations_data = json.load(file)
            if not isinstance(evaluations_data, list):
                raise ValueError("JSON文件内容应为列表")
            return evaluations_data
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"加载JSON文件时出错: {e}")
        return []


# 将评价对象列表转换为可JSON存储的数据结构并保存到JSON文件
def save_evaluations_to_json(file_path: str, evaluations: List[Evaluation]) -> None:
    """
    将评价数据保存到JSON文件
    参数:
        file_path 文件路径 str
        evaluations 评价对象列表 List[Evaluation]
    无返回
    """
    try:
        evaluations_data = [evaluation.to_dict() for evaluation in evaluations]
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(evaluations_data, file, ensure_ascii=False, indent=4)
    except (IOError, TypeError) as e:
        print(f"保存JSON文件时出错: {e}")


# 将JSON数据转换为评价对象列表
def convert_to_evaluations(evaluations_data: List[Dict[str, Any]]) -> List[Evaluation]:
    """
    转换JSON数据为评价对象列表
    参数:
        evaluations_data 评价数据的字典列表 List[Dict[str, Any]]
    返回:
        评价对象列表 List[Evaluation]
    """
    evaluations = []
    for data in evaluations_data:
        try:
            if not isinstance(data, dict):
                raise ValueError("每个评价数据应为字典")
            date = datetime.fromisoformat(data['date'])
            dish = data['dish']
            student_id = data['student_id']
            content = data['content']
            evaluation = Evaluation(date, dish, student_id, content)
            evaluations.append(evaluation)
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            print(f"数据转换时出错: {e}")
    return evaluations