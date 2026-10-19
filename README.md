# 零基础统计学习指南

配套 Python 代码、Notebook 与学习练习。

- [在线代码网站](https://1205103295.github.io/statistical-learning-guide/)
- [v1 第二章代码目录](https://1205103295.github.io/statistical-learning-guide/v1/)
- [2.1.2 配套 Notebook](docs/v1/notebooks/ch02/2.1.2-estimating-f.ipynb)

当前收录 2.1.2「如何估计 f？」的 9 个代码块，包含线性回归、KNN 回归及实际运行结果和图形。

## 使用方法

点击 PDF 代码框右上角的“打开并复制”，在网页中复制对应代码块；也可下载完整 Notebook，在 VS Code 的 Jupyter 环境中从上到下运行。后面的代码块依赖前面已经定义的变量。

Notebook 使用本节五个教学数据点，无须下载外部数据。第 9 块代码会在运行目录下创建“图片”文件夹。

已验证 Python 3.10.20，依赖版本见 [requirements.txt](docs/v1/requirements.txt)。在你的 Python 环境安装这些依赖后，使用 VS Code 的 Python 和 Jupyter 扩展打开 Notebook 并选择对应内核。

## 发布与版本

GitHub Pages 发布源：`main` 分支的 `/docs` 目录。
PDF 指向 `v1/ch02/code/212-01.html` 等固定版本地址。内部文件名与 PDF 展示编号的对应关系见 [manifest.json](docs/v1/manifest.json)。
后续改变代码含义时建立新版本目录，保留旧版地址，以便已分享的 PDF 继续找到匹配代码。

本仓库发布配套代码、Notebook 与生成图形。原教材、手写笔记和本地审核稿不包含在内。

## 2.3 Python 实验

- [42个实验代码块](https://1205103295.github.io/statistical-learning-guide/v1/python-lab.html)
- [完整已执行 Notebook](docs/v1/notebooks/ch02/2.3-python-lab.ipynb)

根据手稿整理数组、切片、布尔索引、pandas清洗、绘图与完整预测流程。每块配有中文解释和实际输出，Notebook还包含小节练习与答案。全部数据为教学用虚构数据，不是真实Auto数据项目。需要从头顺序运行，图片保存到工作目录下的“图片”目录。

代码版本继续使用v1，仅追加新编号231—239，原2.1.2链接不变。
