# -------------------------------------------------------------------------------
# Name:        pdf2svg
# Purpose:     Convert PDF files to svg files.
#
# Author:      chenjunhan
#
# Created:     05/12/2023
# Copyright:   (c) chenjunhan 2023
# Licence:     MIT
# -------------------------------------------------------------------------------
"""
Convert PDF files to svg files.
"""

from pathlib import Path

import fitz
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox


def main():
    """
    Convert PDF files to svg files.
    """
    app = QApplication([])
    widget = QWidget()

    files, _ = QFileDialog.getOpenFileNames(
        widget, "Select PDF Files", "", "PDF Files (*.pdf)"
    )
    if not files:
        QMessageBox.information(
            widget,
            "Information",
            "The file to be converted are not selected!",
            QMessageBox.StandardButton.Ok,
        )
        return

    print("The following files will be converted:")
    for file in files:
        print(file)
    print("Select the output directory:")

    destination = QFileDialog.getExistingDirectory(widget, "Select Directory")
    if not destination:
        QMessageBox.information(
            widget,
            "Information",
            "The output directory is not selected!",
            QMessageBox.StandardButton.Ok,
        )
        return
    print(destination)
    print("-" * 30)
    destination = Path(destination)

    # Start performing the conversion.
    for file in files:
        print(f"Converting: {file}")

        with fitz.open(file) as document:
            document_path = Path(file)
            page_count = document.page_count

            for page_index in range(page_count):
                page = document[page_index]
                svg_page = page.get_svg_image()

                svg_file_name = f"{document_path.stem}_{page_index}.svg"

                with (destination / Path(svg_file_name)).open(
                    "w", encoding="utf-8"
                ) as svg_file:
                    svg_file.write(svg_page)

                print(f"{page_index+1}/{page_count}")

            print("-" * 30)

    print("All files have been converted!")
    input("Press any key...")

    app.quit()


if __name__ == "__main__":
    main()
