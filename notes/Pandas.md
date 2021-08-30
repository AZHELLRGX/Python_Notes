# 环境准备

## 安装Jupyter Notebook

```shell
# 安装Jupyter Notebook，使用清华大学下载源加快下载速度
pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple 

# 安装 Jupyter Lab 的命令如下
pip install jupyterlab
```

## 启动Jupyter Notebook

```shell
Jupyter Notebook
# 如果安装的是Jupyter Lab；就使用如下命令
Jupyter Lab
```

## 安装pandas

```shell
# 可指定国内源快速下载安装
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```

在使用Pandas过程中会用到一些专门的库，如Excel读取生成、可视化等功能，方便起见，可以将后期会用到的其他包一次性安装好

> Excel处理相关包：xlrd、openpyxl、XlsxWriter
>
> 解析网页包：Requests、lxml、html5lib、Beautiful Soup 4
>
> 可视化包：Matplotlib、seaborn、Plotly、Bokeh
>
> 计算包：SciPy、statsmodels

```shell
pip install xlrd openpyxl xlsxwriter requests lxml html5lib BeautifulSoup4 \
matplotlib seaborn plotly bokeh scipy statsmodels -i \
https://pypi.tuna.tsinghua.edu.cn/simple
```

## 快速入门

可以在网址 `https://www.gairuo.com/file/data/dataset/team.xlsx` 下载所需的数据集

## PyCharm三方库代码提示问题的解决方法

[Pycharm 有些库（函数）没有代码提示，没有智能提示，仅仅为自己查找方便使用 - 程序员大本营 (pianshen.com)](https://www.pianshen.com/article/2583965952/)

