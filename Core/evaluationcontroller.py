
# 提供以下接口：
# - add_evaluation(dish: str, evaluator_id: str, content: str) -> None: 添加评价
# - find_evaluation_by_id(evaluator_id: str) -> List[Evaluation]: 根据评价人学号查找评价
# - find_evaluation_by_content(content: str) -> List[Evaluation]: 根据评价内容查找评价
# - get_all_evaluations() -> List[Evaluation]: 获取所有评价
# - remove_evaluation(evaluator_id: str, content: str) -> None: 根据评价人学号和评价内容删除评价
# - update_evaluation(evaluator_id: str, old_content: str, new_content: str) -> None: 更新评价


from typing import List
from Core.StudentEvaluation import Evaluation


class EvaluationInterface:
    def __init__(self, evaluation_controller):
        self.evaluation_controller = evaluation_controller

    def add_evaluation(self, dish: str, evaluator_id: str, content: str) -> None:
        """
        接口：添加评价
        参数:
            dish: 菜品名称
            evaluator_id: 评价人学号
            content: 评价内容
        """
        self.evaluation_controller.add_evaluation(dish, evaluator_id, content)

    def find_evaluation_by_id(self, evaluator_id: str) -> List[Evaluation]:
        """
        接口：根据评价人学号查找评价
        参数:
            evaluator_id: 评价人学号
        返回:
            符合条件的评价列表 List[Evaluation]
        """
        return self.evaluation_controller.find_evaluation_by_id(evaluator_id)

    def find_evaluation_by_content(self, content: str) -> List[Evaluation]:
        """
        接口：根据评价内容查找评价
        参数:
            content: 评价内容
        返回:
            符合条件的评价列表 List[Evaluation]
        """
        return self.evaluation_controller.find_evaluation_by_content(content)

    def get_all_evaluations(self) -> List[Evaluation]:
        """
        接口：获取所有评价
        """
        return self.evaluation_controller.get_all_evaluations()

    def remove_evaluation(self, evaluator_id: str, content: str) -> None:
        """
        接口：根据评价人学号和评价内容删除评价
        参数:
            evaluator_id: 评价人学号
            content: 评价内容
        """
        self.evaluation_controller.remove_evaluation(evaluator_id, content)

    def update_evaluation(self, evaluator_id: str, old_content: str, new_content: str) -> None:
        """
        接口：更新评价
        参数:
            evaluator_id: 评价人学号
            old_content: 原评价内容
            new_content: 新评价内容
        """
        self.evaluation_controller.update_evaluation(evaluator_id, old_content, new_content)