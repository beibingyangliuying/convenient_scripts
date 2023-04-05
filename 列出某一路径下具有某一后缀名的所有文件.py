import pathlib
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口
        size = (400, 400)
        self.setWindowTitle('文件名结果')
        self.setGeometry(100, 100, *size)
        self.setFixedSize(*size)

        # 添加勾选框
        self.checkbox = QCheckBox('显示相对路径', self)
        self.checkbox.move(20, 20)

        # 添加文本输入框
        size = (360, 320)
        self.textedit = QPlainTextEdit(self)
        self.textedit.move(20, 60)
        self.textedit.setReadOnly(True)
        self.textedit.resize(*size)

        # 关联事件
        self.checkbox.stateChanged.connect(self.on_checkbox_stateChanged)

    @pyqtSlot(int)
    def on_checkbox_stateChanged(self, state):
        """
        更新lineedit的显示，以显示相对路径或绝对路径
        :param state: 勾选框状态，选中或未选中
        """
        if state == Qt.CheckState.Checked.value:
            self.textedit.setPlainText(
                '\n'.join([str(file.relative_to(root_path)) for file in path.glob('*.{0}'.format(suffix))]))
        else:
            self.textedit.setPlainText('\n'.join([str(file) for file in path.glob('*.{0}'.format(suffix))]))


app = QApplication([])
window = MainWindow()

root_path = QFileDialog.getExistingDirectory(caption="选择文件夹", options=QFileDialog.Option.ShowDirsOnly)
path = pathlib.Path(root_path)

if not path.exists():
    QMessageBox.warning(window, "警告", "指定文件夹不存在！")
    exit(1)

suffix, ok = QInputDialog.getText(window, '输入框', '请输入文件后缀名：')
if not ok:
    QMessageBox.information(window, '信息', '未输入后缀名！程序终止！')
    exit(0)

window.show()
sys.exit(app.exec())
