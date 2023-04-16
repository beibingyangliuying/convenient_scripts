import unittest


class FileTransformerTestcase(unittest.TestCase):
    def test_ui(self):
        from MyInterfaces.FileTransformer.Interface import Interface
        from PyQt6.QtWidgets import QApplication

        app = QApplication([])
        ui = Interface()
        ui.show()

        self.assertEqual(app.exec(), 0)


if __name__ == '__main__':
    unittest.main()
