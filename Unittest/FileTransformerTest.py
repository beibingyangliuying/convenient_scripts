import unittest


class FileTransformertestcase(unittest.TestCase):
    def test_init_ui(self):
        from MyInterfaces.FileTransformer.Pdf2SvgTransformer import Pdf2SvgTransformer
        from PyQt6.QtWidgets import QApplication

        app = QApplication([])
        window = Pdf2SvgTransformer()
        window.show()
        exit(app.exec())


if __name__ == '__main__':
    unittest.main()
