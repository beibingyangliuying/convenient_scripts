import bibtexparser
import re
from PyQt6.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget

# 创建Qt应用程序对象
app = QApplication([])
widget = QWidget()

# 弹出文件对话框
file_path, _ = QFileDialog.getOpenFileName(None, '打开.bib文献数据库', '', 'bib文件 (*.bib)')

# 读取BibTeX文件
try:
    with open(file_path, encoding='utf-8') as f:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.load(f, parser=parser)
except FileNotFoundError:
    QMessageBox.warning(widget, 'Warning', '指定文件不存在！进程终止！')
    exit(1)

# 遍历条目，修改ID
for entry in bib_database.entries:
    authors = re.split(' and ', entry['author'])
    first_author = re.sub('[ ,\-\{\}]', '_', authors[0])
    first_author = re.sub('[\_]+', '_', first_author)

    title = re.sub('[ ,\-\{\}]', '_', entry['title'])
    title = re.sub('[\_]+', '_', title)

    entry['ID'] = title + '_' + first_author
    entry['maxnames'] = '1'

# 将修改后的条目保存到新的BibTeX文件中
with open(file_path, mode='w', encoding='utf-8') as f:
    bibtexparser.dump(bib_database, f)

# 程序终止
QMessageBox.information(widget, 'End', '文献标识符已格式化完毕！')
