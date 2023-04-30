from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from .FileTransformer import Ui_Dialog
from .Context import Context
from pathlib import Path


class Interface(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # 文件转换上下文
        self.context = Context()

        # 绑定模型和视图
        self.file_paths = QStringListModel()
        self.ui.listView_in_files.setModel(self.file_paths)

        self.ui.comboBox_in_type.setModel(QStringListModel(Context.supported.keys()))

    def on_add_files(self) -> None:
        """
        添加需要转换的文件
        """
        file_type = self.ui.comboBox_in_type.currentText()
        file_paths, _ = QFileDialog.getOpenFileNames(self, "请选择{0}文件".format(file_type), "",
                                                     "{0} 文件 (*.{0})".format(file_type))
        if not file_paths:
            QMessageBox.information(self, "信息", "未添加文件！")
            return

        str_list = self.file_paths.stringList()
        str_list.extend(file_paths)
        str_list = list(set(str_list))
        self.file_paths.setStringList(str_list)

    def on_do_transform(self) -> None:
        """
        执行文件转换
        """
        in_type = self.ui.comboBox_in_type.currentText()
        out_type = self.ui.comboBox_out_type.currentText()
        out_directory = self.ui.lineEdit_out_directory.text()

        if out_directory == "" or not Path(out_directory).exists():  # 不应接受""为当前工作路径
            QMessageBox.warning(self, "警告", "输出目录：{0}不存在！请重新设置！".format(out_directory))
            return

        # if QMessageBox.information(self, "确认",
        #                            "请确认输出目录：\n{0}".format(out_directory)) != QMessageBox.StandardButton.Ok:
        #     return

        try:
            succeed = self.context.execute_strategy(in_type, out_type, self.file_paths.stringList(), out_directory)
            QMessageBox.information(self, "信息", "转换成功！成功转换{0}个文件。".format(succeed))
            self.file_paths.setStringList([])
        except KeyError as e:
            QMessageBox.warning(self, "警告", e.args[0])

    def on_set_out_directory(self) -> None:
        """
        设置输出目录
        """
        out_directory = QFileDialog.getExistingDirectory(self, "请选择输出目录", "", QFileDialog.Option.ShowDirsOnly)
        if out_directory:
            self.ui.lineEdit_out_directory.setText(out_directory)

    def on_remove_files(self) -> None:
        """
        移除已添加的文件
        """
        indexes = self.ui.listView_in_files.selectedIndexes()

        if not indexes:
            QMessageBox.information(self, "信息", "请选择需要移除的文件！")
            return

        rows = [index.row() for index in indexes]
        rows.sort(reverse=True)  # 必须要从后往前移除
        for row in rows:
            self.file_paths.removeRow(row)

    def on_in_type_changed(self) -> None:
        """
        输入文件格式改变时，清空已添加的文件
        """
        self.file_paths.setStringList([])
        in_type = self.ui.comboBox_in_type.currentText()
        self.ui.comboBox_out_type.setModel(QStringListModel(Context.supported[in_type].keys()))
