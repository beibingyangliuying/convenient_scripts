from .Strategy import *


class Context:
    supported = {"pdf": {"svg": Pdf2SvgStrategy}}

    def __init__(self) -> None:
        self.strategy = None

    def set_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def execute_strategy(self, in_type: str, out_type: str, file_paths: list[str], out_directory: str) -> int:
        """
        执行文件转换算法
        :raise KeyError: 请求不支持的文件转换操作时抛出
        """
        try:
            class_type = self.supported[in_type][out_type]
            strategy = class_type()
            self.set_strategy(strategy)
        except KeyError as e:
            raise KeyError("不支持从{0}格式到{1}格式的转换！".format(in_type, out_type)) from e

        return self.strategy.do_transform(file_paths, out_directory)
