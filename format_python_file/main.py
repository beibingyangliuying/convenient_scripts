import os
from pathlib import Path
from typing import Generator

import black
import isort


def traverse_directory(directory: str, suffix: str) -> Generator[Path, None, None]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(f".{suffix}"):
                yield Path(os.path.join(root, file))


def main() -> None:
    directory = Path(input("Please enter the directory that contains python files: "))
    if not directory.exists() or not directory.is_dir():
        print(f"The directory: {directory} is not valid!")
        return

    files = list(traverse_directory(directory, "py"))
    if not len(files):
        print("No python files!")
        return

    for file in files:
        print(f"Formatting: {file}.")

        isort.file(file)
        with open(file, "r") as f:
            code = f.read()
        formatted_code = black.format_str(code, mode=black.Mode())
        with open(file, "w") as f:
            f.write(formatted_code)

        print("Succeed.\n")

    print("Done!")


if __name__ == "__main__":
    main()
