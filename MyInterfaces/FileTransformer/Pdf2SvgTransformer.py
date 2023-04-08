from .AbstractTransformer import AbstractTransformer
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import pathlib
import fitz


class Pdf2SvgTransformer(AbstractTransformer):
    def __init__(self):
        AbstractTransformer.__init__(self, 'pdf', 'svg')

    def do_transform(self) -> None:
        output_path = pathlib.Path(self.output_path)
        if not output_path.exists():
            QMessageBox.warning(self, '警告', '输出目录无效！请重新设定！')
            return

        str_list = self.file_paths.stringList()
        if not str_list:
            QMessageBox.warning(self, '警告', '没有需要执行转换的文件！')
            return

        succeed = 0
        for string in str_list:
            file_path = pathlib.Path(string)

            if not file_path.exists():
                continue

            with fitz.open(file_path) as document:
                for page_index in range(document.page_count):
                    page = document[page_index]
                    svg_page = page.get_svg_image()
                    with (output_path / pathlib.Path('{0}_{1}.svg'.format(file_path.stem, page_index))).open('w',
                                                                                                             encoding='utf-8') as f:
                        f.write(svg_page)

            succeed += 1

        QMessageBox.information(self, '信息', '文件转换已完成！\n已完成{0}项转换。'.format(succeed))

    def add_files(self) -> None:
        file_paths, _ = QFileDialog.getOpenFileNames(None, '选择{0}文件'.format(self.input_type), '',
                                                     '{0}文件(*.{0})'.format(self.input_type))
        if not file_paths:
            QMessageBox.information(self, '信息', '未添加文件！')
            return

        str_list = self.file_paths.stringList()
        str_list.extend(file_paths)
        self.file_paths.setStringList(list(set(str_list)))  # 保证文件路径的唯一性

    def remove_files(self) -> None:
        selected_indexes = self.listview_input.selectedIndexes()
        str_list = self.file_paths.stringList()

        if not selected_indexes:
            QMessageBox.information(self, '信息', '请选择文件！')
            return

        for index in selected_indexes:
            str_list.remove(self.file_paths.data(index, Qt.ItemDataRole.DisplayRole))

        self.file_paths.setStringList(str_list)

    def set_output_path(self) -> None:
        self.output_path = QFileDialog.getExistingDirectory(caption="选择文件夹",
                                                            options=QFileDialog.Option.ShowDirsOnly)
        self.lineedit_output.setText(self.output_path)
