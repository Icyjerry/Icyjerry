<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Jerry Hu / Icyjerry — Software Engineering at Fudan. From the model to the machine.">
</picture>

<img align="right" src="assets/jerry.png" width="180" alt="Jerry inspecting a computer cable">

我是 Jerry，复旦大学软件工程本科生。

最近在沿着 **LLM → Systems** 这条线往下学：从一个 token 怎么变成 logits，到训练和推理时，计算、内存和硬件分别在做什么。

我喜欢把不太懂的东西拆小，写一遍，再做成能跑的实验或能看懂的教程。

[项目 / Projects](#on-the-workbench) · [工具 / Tools](#tools-i-reach-for) · [动态 / Activity](#from-github)

## Going down the stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/learning-path-dark.svg">
  <img src="assets/learning-path-light.svg" width="100%" alt="学习路线：CS61 系列、CS170 与 CSAPP 基础 → micrograd / makemore → GPT 与 BPE → LLM 训练 → 后训练 → CS336、推理与 AI Infra。这是学习方向，不代表课程已全部完成。">
</picture>

### Current focus

| 状态 | 最近关心的问题 | 线索 |
| :--- | :--- | :--- |
| `learning` | 一个 Transformer 的前向传播，每一步到底算了什么？ | Karpathy 系列 · GPT / nanoGPT · BPE |
| `practicing` | 微调改变了什么，模型又会在哪些样本上出错？ | PyTorch · Hugging Face · 分类实验 |
| `foundations` | 从程序到机器，数据怎么表示、移动和计算？ | CS61 系列 · CS170 · CSAPP |
| `next` | 训练和推理的开销在哪里，怎么测、怎么优化？ | CS336 · LLM systems · AI infra |

<details>
<summary>展开学习路线 / reading &amp; building notes</summary>

- **程序与系统基础**：CS61A / CS61B / CS61C、CS170、CSAPP；公开记录见 [CS61A](https://github.com/Icyjerry/cs61a-projects) 和 [CS61B](https://github.com/Icyjerry/CS61B)。
- **从零理解模型**：沿 Karpathy 的 micrograd、makemore、GPT / nanoGPT、tokenizer / BPE、GPT-2 reproduction 路线学习。
- **训练与后训练**：用 PyTorch、Hugging Face 做实验，继续了解 LLM fine-tuning / post-training。
- **往下探索**：为 CS336 补基础，逐步学习推理、内存、runtime 和分布式训练。

这里记录学习方向；没有把课程、教程或计划写成已完成的成果。

</details>

## On the workbench

<table>
<tr>
<td width="50%" valign="top">
<sub>01 / OPEN THE MODEL</sub>
<h3><a href="https://github.com/Icyjerry/transformer-32-vocab-tutorial">32 词表 Transformer</a></h3>
<p>把一次前向传播拆到张量形状：embedding、attention、MLP，再到 logits。附可运行的 PyTorch 示例。</p>
<code>PyTorch</code> <code>shapes &amp; attention</code>
</td>
<td width="50%" valign="top">
<sub>02 / RUN THE EXPERIMENT</sub>
<h3><a href="https://github.com/Icyjerry/distilbert-emotion-classification-lab">DistilBERT 情绪分类</a></h3>
<p>从特征提取到微调，再回头看错误样本。记录模型怎么用，以及实验结果怎么读。</p>
<code>Hugging Face</code> <code>fine-tuning</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<sub>03 / MEASURE THE CODE</sub>
<h3><a href="https://github.com/Icyjerry/cpp-sorting-experiment">C++ 排序实验</a></h3>
<p>归并排序的小数组换成插入排序，什么时候更快？保留实现、基准数据和分析。</p>
<code>C++</code> <code>algorithms &amp; benchmarks</code>
</td>
<td width="50%" valign="top">
<sub>04 / MAKE IT DO SOMETHING</sub>
<h3><a href="https://github.com/Icyjerry/mahjong-bot">Mahjong Bot</a></h3>
<p>从屏幕识别麻将牌，跟踪牌局，再连接策略。把识别、状态和决策放到一起。</p>
<code>Python</code> <code>OpenCV</code>
</td>
</tr>
</table>

<details>
<summary>其他实验、小工具和课程项目</summary>

| 仓库 | 做了什么 |
| :--- | :--- |
| [CIFAR-10 CNN](https://github.com/Icyjerry/cifar10-cnn) | 从 LeNet 到更深的卷积网络，做图像分类练习。 |
| [Fourier Explained](https://github.com/Icyjerry/fourier-explained) | 可以调参数的傅里叶变换讲解网页。 |
| [VR Classroom](https://github.com/Icyjerry/vr-classroom) | Three.js / WebXR 虚拟课堂 demo。 |
| [Game Platform](https://github.com/Icyjerry/game-platform) | Java 课程里的游戏大厅。 |
| [数模 skill](https://github.com/Icyjerry/cumcm-vibecoding) | 整理建模、实验和结果核验流程。 |

</details>

## Tools I reach for

<table>
<tr>
<td width="50%" valign="top">
<strong>Languages</strong><br><br>
<img src="assets/icons/Python-Dark.svg" width="36" alt="Python"> <img src="assets/icons/C.svg" width="36" alt="C"> <img src="assets/icons/CPP.svg" width="36" alt="C++"> <img src="assets/icons/Java-Dark.svg" width="36" alt="Java"> <img src="assets/icons/Bash-Dark.svg" width="36" alt="Shell"><br>
<sub>Python · C / C++ · Java · Shell</sub>
</td>
<td width="50%" valign="top">
<strong>Models &amp; experiments</strong><br><br>
<img src="assets/icons/PyTorch-Dark.svg" width="36" alt="PyTorch"> <img src="assets/icons/Anaconda-Dark.svg" width="36" alt="Conda"><br>
<sub>PyTorch · Hugging Face · Jupyter · Conda / uv</sub>
</td>
</tr>
<tr>
<td valign="top">
<strong>Systems workbench</strong><br><br>
<img src="assets/icons/Linux-Dark.svg" width="36" alt="Linux"> <img src="assets/icons/Bash-Dark.svg" width="36" alt="Bash"><br>
<sub>Linux · shell · computer systems coursework</sub>
</td>
<td valign="top">
<strong>Everyday tools</strong><br><br>
<img src="assets/icons/Git.svg" width="36" alt="Git"> <img src="assets/icons/VSCode-Dark.svg" width="36" alt="VS Code"> <img src="assets/icons/Idea-Dark.svg" width="36" alt="JetBrains IDEA"><br>
<sub>Git · VS Code · JetBrains</sub>
</td>
</tr>
</table>

## From GitHub

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github/stats-dark.svg">
  <img src="assets/github/stats-light.svg" width="49%" alt="GitHub statistics: stars, commits, pull requests, issues and contributions">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github/languages-dark.svg">
  <img src="assets/github/languages-light.svg" width="49%" alt="Language distribution across public repositories, excluding this profile repository">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github/streak-dark.svg">
  <img src="assets/github/streak-light.svg" width="100%" alt="Current contribution streak, longest streak and total contributions within the past-year calendar">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github/activity-dark.svg">
  <img src="assets/github/activity-light.svg" width="100%" alt="GitHub contribution activity for the last 31 days">
</picture>

<sub>每日更新。语言占比来自公开仓库代码量（不含本主页），不代表熟练度。连续贡献统计范围为近一年；今天尚无贡献时，连续天数可延续到昨天。</sub>

---

欢迎在具体项目里提 issue，讨论实现、实验结果，或者哪里还没讲清楚。

<sub><a href="MAINTENANCE.md">About this README / assets &amp; data sources</a></sub>
