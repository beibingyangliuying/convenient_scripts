from abc import abstractmethod
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import pathlib


class AbstractTransformer(QMainWindow):
    def __init__(self, input_type: str, output_type: str):
        super().__init__()

        self.file_paths = QStringListModel([])
        self.input_type = input_type
        self.output_type = output_type
        self.output_path = str(pathlib.Path.cwd())

        self.init_ui()
        self.init_action()
        self.init_connection()

    @abstractmethod
    def do_transform(self) -> None:
        pass

    @abstractmethod
    def add_files(self) -> None:
        pass

    @abstractmethod
    def remove_files(self) -> None:
        pass

    @abstractmethod
    def set_output_path(self) -> None:
        pass

    def init_ui(self) -> None:
        # 主窗口
        self.setWindowTitle('{0}至{1}文件转换器'.format(self.input_type, self.output_type))
        self.setFixedSize(400, 400)

        # 添加文件按钮
        self.button_add_files = QPushButton('添加文件', self)
        self.button_add_files.move(10, 10)

        # 移除文件按钮
        self.button_remove_files = QPushButton('移除文件', self)
        self.button_remove_files.move(120, 10)

        # 转换文件按钮
        self.button_do_transform = QPushButton('转换', self)
        self.button_do_transform.move(230, 10)

        # 待转换文件列表视图
        self.listview_input = QListView(self)
        self.listview_input.setGeometry(QRect(10, 50, 380, 280))
        self.listview_input.setModel(self.file_paths)
        self.listview_input.setSelectionMode(QListView.SelectionMode.MultiSelection)

        label = QLabel('输出目录：', self)
        label.setGeometry(QRect(10, 350, 60, 20))

        # 输出目录编辑器
        self.lineedit_output = QLineEdit(self)
        self.lineedit_output.setGeometry(QRect(80, 350, 300, 20))
        self.lineedit_output.setReadOnly(True)
        self.lineedit_output.setText(self.output_path)

        # 自定义快捷键菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

    def init_connection(self) -> None:
        self.button_add_files.clicked.connect(self.action_add_files.trigger)
        self.button_do_transform.clicked.connect(self.action_do_transform.trigger)
        self.button_remove_files.clicked.connect(self.action_remove_files.trigger)

        self.action_add_files.triggered.connect(self.add_files)
        self.action_remove_files.triggered.connect(self.remove_files)
        self.action_do_transform.triggered.connect(self.do_transform)
        self.action_set_output_directory.triggered.connect(self.set_output_path)

        self.customContextMenuRequested.connect(self.show_custom_menu)

    def init_action(self):
        self.action_add_files = QWidgetAction(self)
        self.action_add_files.setText('添加文件')

        self.action_remove_files = QWidgetAction(self)
        self.action_remove_files.setText('移除文件')

        self.action_do_transform = QWidgetAction(self)
        self.action_do_transform.setText('执行转换')

        self.action_set_output_directory = QWidgetAction(self)
        self.action_set_output_directory.setText('设置输出目录')

    def show_custom_menu(self, pos: QPoint):
        menu = QMenu('文件操作菜单', self)
        menu.addAction(self.action_add_files)
        menu.addAction(self.action_remove_files)
        menu.addAction(self.action_do_transform)
        menu.addAction(self.action_set_output_directory)
        menu.move(self.mapToGlobal(pos))
        menu.show()
