# Welcome

This is `convenient_scripts`, the purpose of this toolkit is to simplify daily workflow by providing some ready-to-use scripts.

The codes are separated by directories, and the name of the directory clearly indicates the purpose. Just run `main.py` in the directory.

Here are shortly descriptions of them:

- `convert_document`: Aiming at converting the format of files.
- `format_bibitem_id`: Aiming at formatting the `ID` of the entries in `.bib` file using `title` and `authors`.

## `convert_document`

Sometimes I am using `tikz` to generate graphs. But I need a tool to convert `.pdf` files to `.png` files so that I can insert the images into a `word` document. That's why I write this tool. More format conversions may be by supported in the future. Here are currently supported conversions:

- `.pdf`->`.png`,`.svg`.

## `format_bibitem_id`

I use `Zotero` to manage references. But when I'm using writing program like `LaTex` or `Typst`, I need to export selected entries from `Zotero` as `.bib` file. Unfortunately, the `IDs` of the exported entries tend to be **messy**, which makes it difficult to manage and cite references. So I wrote this tool to manage reference IDs, and it works by utilizing the title of the document with the first author.

Here is the example:

```bibtex
@article{Note_on_the_Distribution_of_the_Largest_Value_of_a_Random_Function_with_Application_to_Gust_Loading_Davenport_Alan_G,
 author = {Davenport, Alan G},
 date = {1964},
 journaltitle = {Proceedings of the Institution of Civil Engineers},
 pages = {187--196},
 title = {Note on the Distribution of the Largest Value of a Random Function with Application to Gust Loading},
 volume = {28}
}

@article{Statistical_Characterization_of_Strong_Ground_Motions_Using_Power_Spectral_Density_Function_Lai_Shih_sheng_Paul,
 author = {Lai, Shih-sheng Paul},
 date = {1982},
 journaltitle = {Bulletin of the Seismological Society of American},
 number = {1},
 pages = {259--273},
 title = {Statistical Characterization of Strong Ground Motions Using Power Spectral Density Function},
 volume = {72}
}

@article{与规范反应谱相对应的Clough_Penzien模型参数研究_张猛,
 abstract = {根据我国现行抗震规范({GB}50011-2001)的反应谱曲线,对Clough-Penzien模型的参数取值进行了具体研究.采用时间包络函数考虑地震动的非平稳性,根据加速度峰值等效原则确定了谱强度因子S0的表达式,表明谱强因子不仅与地面加速度特性、场地类别有关,而且与结构的动力特性(阻尼比、自振周期)有关.最后对谱强度因子计算做了简化处理,为随机抗震计算分析提供了参考依据.},
 author = {{张猛} and {张哲} and {李天}},
 date = {2007},
 journaltitle = {世界地震工程},
 langid = {pinyin},
 number = {1},
 pages = {56--60},
 title = {与规范反应谱相对应的Clough-Penzien模型参数研究},
 volume = {23}
}

@misc{建筑抗震设计规范_中华人民共和国住房和城乡建设部,
 author = {{中华人民共和国住房和城乡建设部}},
 date = {2010-12-01},
 location = {北京},
 publisher = {中国建筑工业出版社},
 title = {建筑抗震设计规范},
 version = {{GB}/T 50011-2010}
}

@article{新抗震规范地震动功率谱模型参数的研究_张治勇,
 abstract = {根据我国抗震规范,建筑抗震设计规范,({GBJ}11-89)将建筑场地分为4类的事实,确定了对应4{类建筑场地的过滤Gauss白噪声过程功率谱密度函数}(Kanai-Tajimi谱)的参数值,并导出了Kanai-Tajimi谱的谱强度与最大地面运动加速度均值,地震烈度及地震影响系数最大值的关系,这与我国新抗震规范建筑场地类别的划分相协调,便于实际应用.},
 author = {{张治勇} and {孙柏涛} and {宋天舒}},
 date = {2000},
 journaltitle = {世界地震工程},
 langid = {pinyin},
 number = {3},
 pages = {33--38},
 title = {新抗震规范地震动功率谱模型参数的研究},
 volume = {16}
}

@article{高层建筑随机地震反应的简捷计算_陈国兴,
 abstract = {依据高层建筑的变形特征,将高层建筑简化为悬臂剪切梁、弯曲梁、弯剪梁和弯曲-剪切梁,给出了其振型函数和相应的计算参数;基于振型叠加原理,给出了高层建筑随机地震反应计算的一般化方法,且为完全二次项组合{CQC法},对不同类型的高层建筑,计算方法的差异仅在于振型函数的差异.最后,对某30层高层建筑进行了随机地震反应数值分析,得到了一些有益的结论.},
 author = {{陈国兴} and {金永彬} and {宰金珉}},
 date = {1999},
 journaltitle = {南京建筑工程学院学报},
 langid = {pinyin},
 number = {1},
 pages = {29--37},
 title = {高层建筑随机地震反应的简捷计算}
}
```
