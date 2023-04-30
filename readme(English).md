# Introduction

This repository is intended to provide a number of ready to use Python scripts which can be performed with a properly
configured Python environment.

The individual scripts are relatively independent, their usages are pointed out through filenames.

If still in doubt, you can check the purpose of each script by looking at the [General.md]() in the Documents folder.

# Environment Configuration

Please refer to [references.txt](https://github.com/beibingyangliuying/convenient_scipts/blob/master/requirements.txt)
for environment configuration. The version of Python I am currently using is 3.10.

After downloading and installing Python, you can configure the Python environment via Powershell (remember to add Python
to the environment variables):

```powershell
pip install -r requirements.txt
```

If you need to access a mirror site, as follows:

```powershell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# Help

Feel free to ask or suggest on the issue board!

# About

The explanation of each folder is as follows:

- UnitTest: Unit tests for each package within MyInterfaces.
- Ui: Qt Designer is used to design the interface and store the `.ui` files.
- MyInterfaces: Contains each interface class and its related classes.
- Documents: Documentation that explains in detail the purpose of each package in MyInterfaces.