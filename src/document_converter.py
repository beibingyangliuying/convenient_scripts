# -------------------------------------------------------------------------------
# Name:        document_converter
# Purpose:     Execute file conversion.
#
# Author:      chenjunhan
#
# Created:     05/12/2023
# Copyright:   (c) chenjunhan 2023
# Licence:     MIT
# -------------------------------------------------------------------------------
"""
Execute file conversion.
"""

from typing import Generator
from pathlib import Path

import fitz
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox


def get_pdf_pages(file: Path) -> Generator[fitz.Page, None, None]:
    """
    Generator function that traverses and generates pdf file pages.
    """
    print(f"Converting: {file.absolute()}")

    if not file.exists():
        print(f"{file.absolute()} not exists!")
        print("-" * 30)
        return

    with fitz.open(str(file)) as document:
        page_count = document.page_count

        for page_index in range(page_count):
            page = document[page_index]
            yield page


def pdf2svg(file: Path, destination: Path):
    """
    Convert each page of the specified pdf file to svg file and save it in the specified directory.
    """
    for count, page in enumerate(get_pdf_pages(file)):
        svg_page = page.get_svg_image()
        svg_file_name = f"{file.stem}_{count}.svg"

        with (destination / Path(svg_file_name)).open(
            "w", encoding="utf-8"
        ) as svg_file:
            svg_file.write(svg_page)
            print(f"Page {count+1} finished.")

    print("-" * 30)


supported = {"pdf": {"svg": pdf2svg}}


def main():
    """
    Perform file conversion.
    """
    app = QApplication([])
    widget = QWidget()

    input_format = input(
        "Please select the input file type:\nOptional: {0}\n".format(",".join(supported))
    )
    print("-" * 30)
    output_format = input(
        "Please select the output file type:\nOptional: {0}\n".format(
            ",".join(supported[input_format])
        )
    )
    print("-" * 30)
    converter = supported[input_format][output_format]

    files, _ = QFileDialog.getOpenFileNames(
        widget,
        f"Select {input_format.upper()} Files",
        "",
        f"{input_format.upper()} Files (*.{input_format})",
    )
    if not files:
        QMessageBox.information(
            widget,
            "Information",
            "The file to be converted are not selected!",
            QMessageBox.StandardButton.Ok,
        )
        return
    files = tuple(Path(file) for file in files)

    print("The following files will be converted:")
    for file in files:
        print(file)
    print("-" * 30)
    print("Select the output directory:")

    destination = QFileDialog.getExistingDirectory(widget, "Select Output Directory")
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
        converter(file, destination)

    print("All files have been converted!")
    input("Press any key...")

    app.quit()


if __name__ == "__main__":
    main()
