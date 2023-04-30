# 简介

本库旨在提供一些开箱即用的Python脚本，只要正确配置Python环境即可运行。

各个脚本都是相对独立的，其用途包含在其文件名中。

如果仍有疑问，可以通过查看Documents文件夹下的[总述.md]()查看各个脚本的用途。

# 环境配置

环境配置文件请参照[references.txt](https://github.com/beibingyangliuying/convenient_scipts/blob/master/requirements.txt)
，我目前使用的Python版本是3.10。

下载并安装Python后，可以通过Powershell配置Python环境（记得将Python添加至环境变量中）：

```powershell
pip install -r requirements.txt
```

如果需要使用镜像网站，如下：

```powershell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 帮助

欢迎在issue板块提出你所遇到的问题或者建议！

# 关于

关于各个文件夹的释义，如下：

- UnitTest：针对MyInterfaces内的各个包进行单元测试。
- Ui： 采用Qt Designer设计界面，存放`.ui`文件。
- MyInterfaces：内含各个界面类及其相关类。
- Documents：文档说明，详细解释MyInterfaces内各个包的用途。
