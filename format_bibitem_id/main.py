import re
import string
from pathlib import Path

import bibtexparser as bibtex
from colorama import init, Fore, Style

init()


def main() -> None:
    path = Path(
        input(
            f"Please input the path of {Fore.YELLOW}.bib{Style.RESET_ALL} file: "
        ).strip("\"'")
    )
    if not path.is_file() or not path.suffix == ".bib":
        print(
            Fore.RED
            + "Please select a valid .bib file! The process is terminated!"
            + Style.RESET_ALL
        )
        return

    with path.open(mode="r", encoding="utf-8") as f:
        parser = bibtex.bparser.BibTexParser(
            ignore_nonstandard_types=False, common_strings=True
        )
        bib_database = bibtex.load(f, parser=parser)

    print("Changes on ID:")
    for entry in bib_database.entries:
        assert isinstance(entry, dict)

        title = format_id(entry["title"])
        authors = [format_id(i.strip("{}")) for i in entry["author"].split(" and ")]
        old_id = entry["ID"]
        new_id = f"{title}_{authors[0]}"
        entry["ID"] = new_id
        print(Fore.BLUE + old_id + "\t->\t" + Fore.GREEN + new_id + Style.RESET_ALL)

    if_ok = input("Confirm format? [y/n]: ")
    assert if_ok == "y" or if_ok == "n"

    if if_ok == "y":
        with path.open(mode="w", encoding="utf-8") as f:
            bibtex.dump(bib_database, f)
            print(Fore.GREEN + "Done!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "The process is terminated!" + Style.RESET_ALL)


def format_id(field: str) -> str:
    pattern = "[" + re.escape(string.punctuation) + r"\s" + "]+"
    return re.sub(pattern, "_", field)


if __name__ == "__main__":
    main()
