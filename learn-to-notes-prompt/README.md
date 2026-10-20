# 从理解到实现：学习与笔记提示词

[复制完整提示词](PROMPT.md) · [配置示例](CONFIG.example.md) · [下载模板与提示词 ZIP](downloads/learn-to-notes-prompt-v1.0.zip) · [查看排版示例](template/main.pdf)

一套可复制的中文学习流程：业务问题 → 概念与假设 → 不跳步推导 → 最小代码 → 完整实践 → 小节反馈 → 手稿成书。

适合希望同时理解数学原理与Python实现的学习者。使用者自行填写基础、教材和目标，不要求特定学历。目录中的材料可直接放入GitHub仓库。

## 快速开始

1. 将PROMPT.md全文复制到新对话。
2. 参考CONFIG.example.md填写自己的配置，提供教材目录和当前材料。
3. 指定本次模式和任务，例如：“复习条件期望，每次只讲一个小环节，先不给练习答案。”
4. 学习告一段落后要求助手按PROGRESS.example.md保存进度。
5. 完整学习一章、提供手稿并授权整理后，再把template目录交给具备文件能力的助手，要求沿用模板生成成果。

最短启动消息：

> 请执行附件PROMPT.md，读取我的配置与进度。本次模式是【学习/整理】，任务是【具体内容】。先核对可访问材料与必要缺项，然后只推进一个获准的学习或整理单元。

提示词不是知识库。新会话仍需教材、手稿和进度；没有代码执行、文件写入、编译或联网能力时，助手应说明限制。不同模型不保证逐字相同或同等教学质量。

## 文件

- PROMPT.md：完整主提示词，包含教学、批改、成书、运行验证和交接。
- CONFIG.example.md：配置示例，使用自己的姓名、路径和环境。
- PROGRESS.example.md：学习与文件状态的交接格式。
- template/：继承原书稿配色、代码框、红色提示、绿色例子、暖米色答案及统计主题封面的可配置模板。
- VALIDATION.md：本包实际验证范围。

## 怎样得到相同风格

不要只让模型“模仿配色”。把template整个目录提供给助手，要求保留guide.sty，编辑config.tex中的书名、作者和版本。正文、代码、讲解、输出分别放入sections、code、explanations、outputs。

封面图案为矢量示意设计，不是研究结果。默认封面适合统计学习；更换为其他学科时应调整主题文案和图案。较长书名需检查封面换行。

同一模板能保持颜色和布局规则一致；字体、编译器版本、内容长度仍会影响分页。代码例子只演示排版和均值计算，不代替正式章节。

## 编译示例

需要XeLaTeX及相应中文字体和宏包（如TeX Live中的ctex、Fandol、tcolorbox、listings、TikZ）。在终端中先进入template目录，确保xelatex已在PATH中：

```text
xelatex -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
xelatex -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
```

生成main.pdf。日常只检查一个代码块可运行：

```text
xelatex -synctex=1 -interaction=nonstopmode -halt-on-error preview.tex
```

生成preview.pdf。两份入口使用同一套样式与内容源；局部预览不代表全书最终分页。默认本地代码按钮依赖copy目录和阅读器本地链接策略。

需要在线版时，把online.tex.example复制为online.tex，替换为自己的已部署HTTPS代码页地址再编译。模板不自动部署网站。网页有复制按钮，浏览器不允许剪贴板访问时可手动复制。

Notebook示例保留未执行状态；输出文本由Python脚本实际执行生成。正式项目应按提示词实际执行相应Notebook并记录环境。

## 如何判断复刻成功

第一次授课没有跳过背景确认，数学符号与前提明确，代码按块讲解，练习能根据回答反馈。成书时正文主要依据笔记，补充有记录，题后有参考答案，代码讲解与实际运行结果对应。

检查红色提示/绿色题目/米色答案/蓝色代码框的区分、完整代码编号、目录、图片、按钮目标和Python输出。学习者能独立完成任务的证据与“已看答案”分开登记。

本仓库材料不包含原教材全文、其他学习者的手稿、个人学习进度或账户信息。公开发布时按自己实际拥有和准备分享的内容选择文件；使用自己的署名和网站地址。
