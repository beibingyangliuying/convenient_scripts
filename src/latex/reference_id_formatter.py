import os
import re
import string

import bibtexparser
from PyQt6.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget


def main() -> None:
    """
    The main function of the application.
    :return: None
    """
    app = QApplication([])
    widget = QWidget()

    file_path, _ = QFileDialog.getOpenFileName(
        widget, "Select .bib reference database", os.getcwd(), "bib file (*.bib)"
    )
    if not file_path:
        QMessageBox.information(
            widget,
            "Information",
            "No file selected! The process is terminated!",
            QMessageBox.StandardButton.Ok,
        )
        return

    with open(file_path, mode="r", encoding="utf-8") as file:
        parser = bibtexparser.bparser.BibTexParser(
            ignore_nonstandard_types=False, common_strings=True
        )
        bib_database = bibtexparser.load(file, parser=parser)

    # Matches one or more consecutive ASCII punctuation marks and whitespace characters.
    pattern = re.compile("[" + re.escape(string.punctuation) + r"\s" + "]+")

    for entry in bib_database.entries:
        title = entry.get("title", "untitled")
        title = clarify(pattern, title)

        authors = entry.get("author", "authorless").split(" and ")
        first_author = authors[0]
        first_author = clarify(pattern, first_author)

        entry["ID"] = title + "_" + first_author

    with open(file_path, mode="w", encoding="utf-8") as file:
        bibtexparser.dump(bib_database, file)

    QMessageBox.information(
        widget, "Information", "Formatted!", QMessageBox.StandardButton.Ok
    )

    app.quit()


def clarify(pattern, field: str):
    return re.sub(pattern, "_", field)


if __name__ == "__main__":
    main()
