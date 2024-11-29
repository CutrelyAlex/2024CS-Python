"""
StudentController 模块

提供以下接口:
- add_student(student: Student): 添加学生
- find_student_by_id(student_id: str) -> Student: 根据学号查找学生
- find_student_by_name(name: str) -> List[Student]: 根据姓名查找学生
- get_all_students() -> List[Student]: 获取所有学生
- remove_student(student_id: str): 根据学号删除学生
- update_student(student_id: str, **kwargs): 更新学生信息
- add_dining_record(student_id: str, dining_info: DiningInfo): 添加餐饮记录
- remove_dining_record(student_id: str, record_id: str): 删除餐饮记录
- find_dining_record(student_id: str, record_id: str) -> DiningInfo: 查找餐饮记录
- update_dining_record(student_id: str, record_id: str, **kwargs): 更新餐饮记录
"""

import re
from typing import List
from Core.StudentModel import Student, convert_to_students, load_students_from_json, save_students_to_json, DiningInfo
from Core.DishModel import *

student_path = "students.json"

class DiningInfo:
    def __init__(self, dining_time: str, dishes: List[Dish], remarks: str, id: str = None, location: str = "Unknown"):
        self.id = id
        self.dining_time = dining_time
        self.dishes = dishes
        self.remarks = remarks
        self.location = location

class StudentController:
    def __init__(self):
        self.students = convert_to_students(load_students_from_json(student_path))
    
    def add_student(self, student: Student):
        """
        添加学生

        参数:
            student (Student): 要添加的学生对象

        无返回
        """
        # ...existing code...
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                raise ValueError("学生已存在")
        self.students.append(student)
        save_students_to_json(student_path, self.students)
    
    def find_student_by_id(self, student_id: str) -> Student:
        """
        根据学号查找学生

        参数:
            student_id (str): 学生的学号

        返回:
            Student: 找到的学生对象
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        raise ValueError("未找到指定的学生")
    
    def find_student_by_name(self, name: str) -> List[Student]:
        """
        根据姓名查找学生

        参数:
            name (str): 学生的姓名

        返回:
            List[Student]: 匹配的学生列表
        """
        pattern = re.compile(name, re.IGNORECASE)
        matched_students = [student for student in self.students if pattern.search(student.name)]
        return matched_students
    
    def get_all_students(self) -> List[Student]:
        """
        获取所有学生

        返回:
            List[Student]: 所有学生列表
        """
        return self.students
    
    def remove_student(self, student_id: str):
        """
        根据学号删除学生

        参数:
            student_id (str): 要删除学生的学号

        无返回
        """
        self.students = [student for student in self.students if student.student_id != student_id]
        save_students_to_json(student_path, self.students)
    
    def update_student(self, student_id: str, **kwargs):
        """
        更新学生信息

        参数:
            student_id (str): 学生的学号
            **kwargs: 需要更新的字段及其新值

        无返回
        """
        for student in self.students:
            if student.student_id == student_id:
                if 'name' in kwargs:
                    student.name = kwargs['name']
                if 'password' in kwargs:
                    student.password = kwargs['password']
                if 'profile' in kwargs:
                    student.profile = kwargs['profile']
                if 'dining_info_list' in kwargs:
                    student.dining_info_list = kwargs['dining_info_list']
                save_students_to_json(student_path, self.students)
                return
        raise ValueError("未找到指定的学生")

    def add_dining_record(self, student_id: str, dining_info: DiningInfo):
        """
        添加餐饮记录

        参数:
            student_id (str): 学生的学号
            dining_info (DiningInfo): 要添加的餐饮记录对象

        无返回
        """
        for student in self.students:
            if student.student_id == student_id:
                student.dining_info_list.append(dining_info)
                save_students_to_json(student_path, self.students)
                return
        raise ValueError("未找到指定的学生")

    def remove_dining_record(self, student_id: str, record_id: str):
        """
        删除餐饮记录

        参数:
            student_id (str): 学生的学号
            record_id (str): 餐饮记录的ID

        无返回
        """
        for student in self.students:
            if student.student_id == student_id:
                original_length = len(student.dining_info_list)
                student.dining_info_list = [
                    record for record in student.dining_info_list if record.id != record_id
                ]
                if len(student.dining_info_list) < original_length:
                    save_students_to_json(student_path, self.students)
                    return
                else:
                    raise ValueError("未找到指定的餐饮记录")
        raise ValueError("未找到指定的学生")

    def find_dining_record(self, student_id: str, record_id: str) -> DiningInfo:
        """
        查找餐饮记录

        参数:
            student_id (str): 学生的学号
            record_id (str): 餐饮记录的ID

        返回:
            DiningInfo: 找到的餐饮记录对象
        """
        for student in self.students:
            if student.student_id == student_id:
                for record in student.dining_info_list:
                    if record.id == record_id:
                        return record
        raise ValueError("未找到指定的餐饮记录")

    def update_dining_record(self, student_id: str, record_id: str, **kwargs):
        """
        更新餐饮记录

        参数:
            student_id (str): 学生的学号
            record_id (str): 餐饮记录的ID
            **kwargs: 需要更新的字段及其新值

        无返回
        """
        for student in self.students:
            if student.student_id == student_id:
                for record in student.dining_info_list:
                    if record.id == record_id:
                        if 'dining_time' in kwargs:
                            record.dining_time = kwargs['dining_time']
                        if 'dishes' in kwargs:
                            record.dishes = kwargs['dishes']
                        if 'remarks' in kwargs:
                            record.remarks = kwargs['remarks']
                        if 'location' in kwargs:
                            record.location = kwargs['location']
                        save_students_to_json(student_path, self.students)
                        return
        raise ValueError("未找到指定的餐饮记录")
