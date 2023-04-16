from abc import abstractmethod, ABC
from pathlib import Path
import fitz


class Strategy(ABC):
    @abstractmethod
    def do_transform(self, file_paths: list[str], out_directory: str) -> int:
        """
        执行文件转换
        :param file_paths: 输入文件路径
        :param out_directory: 输出目录
        :return: 成功转换的文件数
        """
        pass


class Pdf2SvgStrategy(Strategy):
    def do_transform(self, file_paths: list[str], out_directory: str) -> int:
        """
        执行文件转换，将pdf文件转换为svg文件
        :param file_paths: 输入文件路径
        :param out_directory: 输出目录
        :return: 成功转换的文件数
        """
        out_directory = Path(out_directory)

        succeed = 0
        for file_path in file_paths:
            file_path = Path(file_path)

            if not file_path.exists():
                continue

            with fitz.open(file_path) as document:
                for page_index in range(document.page_count):
                    page = document[page_index]
                    svg_page = page.get_svg_image()

                    file_name = "{0}_{1}.svg".format(file_path.stem, page_index)
                    with (out_directory / Path(file_name)).open("w", encoding="utf-8") as file:
                        file.write(svg_page)

            succeed += 1

        return succeed
