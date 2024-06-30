import functools as ft
from pathlib import Path
from typing import Callable, Generator, Union

import fitz
from colorama import init, Fore, Style

init()


def get_suffixed_files(directory: str, suffix: str) -> Generator[Path, None, None]:
    directory = Path(directory)
    return (i for i in directory.iterdir() if i.is_file() and i.suffix == f".{suffix}")


def convert_factory(
    input_format: str, output_format: str
) -> Callable[[str, str], None]:
    """
    Factory function for converting documents.
    :param input_format: Input format.
    :param output_format: Output format.
    :return: Function for converting documents, it receives two arguments: departure and destination, which are strings representing the directories. Keyword-only arguments are supported.
    :raise ValueError: If the conversion is not supported.
    """

    def get_pdf_pages(departure: str) -> Generator[tuple[fitz.Page, Path], None, None]:
        for path in get_suffixed_files(departure, input_format):
            with fitz.open(str(path)) as f:
                if f.page_count != 1:
                    for count, page in enumerate(f.pages()):
                        yield page, Path(f"{path.stem}_{count+1}.{output_format}")
                else:
                    yield f.load_page(0), Path(f"{path.stem}.{output_format}")

    def pdf2svg(departure: str, destination: str) -> None:
        for page, name in get_pdf_pages(departure):
            svg_page = page.get_svg_image()
            with (destination / name).open("w", encoding="utf-8") as f:
                f.write(svg_page)

    def pdf2png(
        departure: str, destination: str, *, dpi: Union[int, str] = 600
    ) -> None:
        for page, name in get_pdf_pages(departure):
            png_page = page.get_pixmap(dpi=int(dpi))
            assert isinstance(png_page, fitz.Pixmap)
            png_page.save(destination / name)

    func = locals().get(f"{input_format}2{output_format}")
    if not func:
        raise ValueError(f"{input_format} to {output_format} not supported.")

    return func


def main() -> None:
    input_format, output_format = input(
        f"Document converter. Please enter the {Fore.YELLOW}input format{Style.RESET_ALL} and {Fore.YELLOW}output format{Style.RESET_ALL} (separated by {Fore.RED}comma{Style.RESET_ALL}): "
    ).split(",")
    func = convert_factory(input_format, output_format)
    departure = input(
        f"Please enter the {Fore.YELLOW}departure directory{Style.RESET_ALL}: "
    ).strip("\"'")
    print("The following files will be converted: ")
    for i in get_suffixed_files(departure, input_format):
        print(Fore.GREEN + str(i) + Style.RESET_ALL)
    if_ok = input("Confirm conversion? [y/n]: ")
    assert if_ok == "y" or if_ok == "n"
    if if_ok == "n":
        print(Fore.RED + "The process is terminated!" + Style.RESET_ALL)
        return

    if func.__kwdefaults__:
        print(
            f"Positional parameters: {Fore.BLUE}{func.__kwdefaults__}{Style.RESET_ALL}"
        )
        arguments = input(
            f'Please enter the values of positional parameters in {Fore.BLUE}"key=value"{Style.RESET_ALL} format and separated by {Fore.RED}comma{Style.RESET_ALL} (press enter to skip):'
        )
        if arguments:
            func = ft.partial(
                func,
                **dict(i.split("=") for i in arguments.split(",")),
            )

    destination = input(
        f'Please enter the {Fore.YELLOW}destination directory{Style.RESET_ALL} (press enter to use "{Fore.GREEN}{departure}{Style.RESET_ALL}"): '
    ).strip("\"'")
    if not destination:
        destination = departure
    func(departure, destination)
    print(Fore.GREEN + "Conversion completed!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
