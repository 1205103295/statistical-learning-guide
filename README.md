# 零基础统计学习指南

配套 Python 代码、Notebook 与学习练习。

## 公开学习提示词与 LaTeX 模板

[使用说明与完整工程](learn-to-notes-prompt/) · [复制主提示词](learn-to-notes-prompt/PROMPT.md) · [下载 ZIP](learn-to-notes-prompt/downloads/learn-to-notes-prompt-v1.0.zip)

复用“业务问题—数学推导—逐块代码—练习反馈—手稿成书”的学习流程。支持填写个人基础、教材和目标，附带可配置封面、红色提示框、浅绿题目、米色答案和蓝色代码框；模板已实际编译。详见工程中的验证记录与行为检查用例。

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

## 2.4 真实Auto项目

[项目代码目录](https://1205103295.github.io/statistical-learning-guide/v1/auto-project.html) · [已执行Notebook](docs/v1/notebooks/ch02/2.4-auto-project.ipynb)

16个代码块，包含固定清洗、三份划分、训练集探索、均值基准、线性回归、标准化KNN、验证选择、开发集重训和最终评估。Notebook首次运行时如无本地数据，将从[教材官网](https://www.statlearning.com/s/Auto.data)下载数据。结果仅用于教学，详见Notebook的适用范围说明。

## 2.4 真实教材章末习题

[项目代码目录](https://1205103295.github.io/statistical-learning-guide/v1/textbook-exercises.html) · [已执行Notebook](docs/v1/notebooks/ch02/2.4-textbook-exercises.ipynb)

29个代码块，对应教材第1—10题，包含示意曲线、KNN手算、College、Auto与Boston数据探索。Notebook首次运行时如无本地数据，将从[教材官网](https://www.statlearning.com/s/Auto.data)下载数据。结果仅用于教学，详见Notebook的适用范围说明。

## 第三章 · 简单线性回归

[在线代码与逐步讲解](https://1205103295.github.io/statistical-learning-guide/v1/ch03.html) · [已执行 Notebook](docs/v1/notebooks/ch03/3.1-simple-linear-regression.ipynb)

18 个代码块：从 NumPy 手算最小二乘系数到残差、RSE、斜率标准误、t 置信区间与双侧假设检验。系数估计实验使用三个市场的虚构数据；检验实验使用虚构拟合汇总量，二者各自独立运行。保留实际执行输出与逐步解释，无须联网下载数据。

[斜率检验 Notebook](docs/v1/notebooks/ch03/3.1.2-slope-testing.ipynb)：四个代码块，依次计算 t 统计量、双侧 p 值、检验结论及对应置信区间。


## 第三章更新：至 3.3.3

已追加模型评估、多元最小二乘与 MP 逆、条件数、t/F 推断、预测区间、类别编码、交互、多项式及六类诊断。43 个代码块在同一新 Jupyter 内核中按顺序执行通过。新增 42 组练习与参考答案。

[完整学习笔记与实验](docs/v1/notebooks/ch03/chapter03-through-3.3.3.ipynb) · [在线代码目录](https://1205103295.github.io/statistical-learning-guide/v1/ch03.html)
