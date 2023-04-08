import fitz
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

app = QApplication([])
widget = QWidget()

file_path, _ = QFileDialog.getOpenFileName(None, '打开pdf文件', '', 'pdf文件(*.pdf)')


def pdf_to_svg(pdf_file, svg_file):
    with fitz.open(pdf_file) as document:
        for page_index in range(document.page_count):
            page = document[page_index]
            svg_page = page.get_svg_image()
            with open(f'{svg_file}_{page_index}.svg', 'w', encoding='utf-8') as f:
                f.write(svg_page)


pdf_to_svg(file_path, 'output')
