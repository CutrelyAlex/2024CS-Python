# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(u"SZTU就餐管理系统")

    # 关闭按钮的提示
    def closeEvent(self, event):
        r = QMessageBox.question(self, "提示：", "确定要关闭吗？", QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
