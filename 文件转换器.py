from MyInterfaces.FileTransformer.Interface import Interface
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    ui = Interface()
    ui.show()
    app.exec()
