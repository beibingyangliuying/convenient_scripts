from pathlib import Path
from typing import Generator

import fitz
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox


def get_pdf_pages(file: Path) -> Generator[fitz.Page, None, None]:
    """
    Get the pages of the PDF file.
    :param file: The PDF file to be converted.
    :type file: Path
    :return: The pages of the PDF file.
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


def pdf2svg(file: Path, destination: Path) -> None:
    """
    Convert the PDF file to SVG.
    :param file: The PDF file to be converted.
    :param destination: The PDF file to be converted.
    :return: None
    """
    for count, page in enumerate(get_pdf_pages(file)):
        svg_page = page.get_svg_image()
        svg_file_name = f"{file.stem}_{count}.svg"

        with (destination / Path(svg_file_name)).open(
                "w", encoding="utf-8"
        ) as svg_file:
            svg_file.write(svg_page)
            print(f"Page {count + 1} finished.")

    print("-" * 30)


def pdf2png(file: Path, destination: Path) -> None:
    """
    Convert the PDF file to PNG.
    :param file: The path to the PDF file to be converted.
    :param destination: The path to the directory where the PNG images will be saved.
    :return: None
    """
    for count, page in enumerate(get_pdf_pages(file)):
        png_page = page.get_pixmap(dpi=300)
        png_file_name = f"{file.stem}_{count}.png"
        png_page.save(destination / Path(png_file_name))

        print(f"Page {count + 1} finished.")

    print("-" * 30)


def svg2pdf(file: Path, destination: Path) -> None:
    """
    Convert the SVG file to PDF.
    :param file: The path to the PDF file to be converted.
    :param destination: The path to the directory where the PNG images will be saved.
    :return: None
    """
    pass


supported = {"pdf": {"svg": pdf2svg, "png": pdf2png}}


def main() -> None:
    """
    The main function of the application.
    :return: None
    """
    app = QApplication([])
    widget = QWidget()

    # Determine the input and output file types.
    input_format = input(
        "Please select the input file type:\nOptional: {0}\n".format(
            ",".join(supported)
        )
    )
    print("-" * 30)
    output_format = input(
        "Please select the output file type:\nOptional: {0}\n".format(
            ",".join(supported[input_format])
        )
    )
    print("-" * 30)
    converter = supported[input_format][output_format]

    # Select the files to be converted.
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

    # Select the output directory.
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
