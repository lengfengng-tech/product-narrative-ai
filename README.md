# ProductNarrative AI

**AI-guided product narratives and executive visual briefs**<br>
**AI 产品方案与商务图解：先讲清业务，再选择视觉主题**

[English](#english) · [中文](#中文文档)

![ProductNarrative AI preview](assets/preview.png)

ProductNarrative AI is an agent skill that turns product material into clear, executive-ready narratives and diagram-led PDFs. It guides AI to own content strategy, information design, visual-theme selection, production, and quality review—rather than mechanically applying a template or running a fixed script.

ProductNarrative AI 是一个面向产品方案、产品概念与管理层汇报的 AI 技能，覆盖资料理解、叙事设计、信息图解、商务主题选择、页面制作与最终评审，不是固定模板或脚本生成器。

- Repository: `product-narrative-ai`
- Internal skill identifier: `product-solution-brief`

---

<a id="english"></a>
## English

### Contents

- [Overview](#overview)
- [Key Capabilities](#key-capabilities)
- [Use Cases](#use-cases)
- [Installation](#installation)
- [Example Prompts](#example-prompts)
- [AI Workflow](#ai-workflow)
- [Visual Design Principles](#visual-design-principles)
- [Project Structure](#project-structure)
- [Optional Scripts](#optional-scripts)
- [Quality Standards](#quality-standards)
- [Contributing](#contributing)

### Overview

ProductNarrative AI helps AI agents produce Chinese product concepts, solution proposals, and executive briefs with a deliberate narrative and a professional visual system.

The skill is built on three principles:

1. **Narrative before layout.** Define the audience, decision context, core argument, and page logic before designing.
2. **Theme by context.** Select a professional visual theme based on industry, brand, audience, and presentation environment; never force a fixed red or blue template.
3. **Review the actual deliverable.** Inspect the final PDF for factual consistency, readability, layout integrity, and visual restraint.

### Key Capabilities

- **AI-led design:** AI determines the audience, communication objective, narrative structure, diagram types, and production route.
- **Conclusion-first storytelling:** Organizes content around why the product matters, how it works, who owns each responsibility, how users reach outcomes, and what value is created.
- **Selectable business themes:** Defines canvas, surfaces, primary color, typography, supporting colors, semantic colors, lines, icons, and spacing as one coherent system.
- **Purposeful diagrams:** Uses relationship maps, business loops, responsibility diagrams, state flows, comparison tables, and case storyboards according to the information—not by habit.
- **Tool-agnostic production:** Supports native layout, vector graphics, presentation tools, PDF workflows, and image generation. Scripts remain optional utilities.
- **Built-in quality review:** Checks Chinese text, numbers, arrows, icon alignment, table layout, cross-page consistency, and final PDF integrity.

### Use Cases

Recommended for:

- Product concepts and solution proposals
- Executive, investor, and client decision briefs
- Product loops, user journeys, and stakeholder responsibilities
- AI capability boundaries and human–AI responsibility models
- Competitive capability mapping and product differentiation
- Diagram-led PDFs for complex business solutions

Not intended for:

- Detailed implementation architecture or API design
- Financial modeling
- Routine copy editing
- Standalone posters or marketing long-form images

### Installation

#### Option 1: Add to an agent skills directory

Clone the repository using the internal skill identifier as the directory name:

```bash
git clone https://github.com/lengfengng-tech/product-narrative-ai.git product-solution-brief
```

Copy the complete `product-solution-brief` directory into the skills directory used by your agent. Ensure the environment can discover `SKILL.md`.

#### Option 2: Build a `.skill` package

From the parent directory of `product-solution-brief`, run:

```bash
zip -r product-solution-brief.skill product-solution-brief \
  -x '*/__pycache__/*' '*.DS_Store'
```

Import `product-solution-brief.skill` through a client that supports `.skill` packages.

### Example Prompts

#### Create an executive product proposal

```text
Use product-solution-brief to create an executive product proposal PDF from the current project materials.
Define the audience and core argument first, then design the narrative and diagrams.
Use a restrained professional business style and select the visual theme according to the content.
```

#### Apply a brand color

```text
Use product-solution-brief to create a product concept brief.
Keep the corporate brand blue as the primary color, with white and neutral gray as the main surfaces.
Use supporting colors only for categories and states. Explain the overall product logic before walking through one consistent user case.
```

#### Produce only the narrative outline

```text
Use the product-solution-brief narrative method to draft a proposal outline.
For each page, provide a conclusion-led title, the question to answer, and the recommended main visual. Do not create a PDF yet.
```

#### Review an existing proposal

```text
Use product-solution-brief to review this product proposal.
Check whether the narrative is conclusion-first, whether colors distract from the content, whether diagrams accurately represent business relationships, and whether later pages become visually inconsistent or overly decorative.
```

### AI Workflow

1. **Frame the task:** Identify the audience, communication objective, usage context, and desired action.
2. **Classify evidence:** Separate confirmed facts, target designs, illustrative data, external information, and open questions.
3. **Design the narrative:** Establish the core argument and page sequence. Each page should communicate one conclusion.
4. **Define the visual theme:** Specify canvas, surfaces, primary color, text, supporting colors, semantic colors, typography, lines, icons, and spacing.
5. **Select the right diagrams:** Match each visual to the underlying information relationship.
6. **Produce and review:** Inspect the cover, the most complex diagram, and the densest page before completing the full set.
7. **Verify the deliverable:** Reopen the final PDF and check page order, aspect ratio, clarity, text, and graphics.

### Visual Design Principles

Professional does not mean monotonous, and consistency does not require every page to use the same color treatment. Every color must have a defined role.

| Visual role | Guidance |
| --- | --- |
| Canvas and surfaces | Use white or neutral tones for most of the area; maintain projection and reading contrast |
| Primary color | Apply to branding, current emphasis, and critical paths; avoid filling every module |
| Body text | Use high-contrast dark text and readable neutral gray for supporting copy |
| Supporting colors | Usually one or two, reserved for stable categories or stakeholder identities |
| Semantic colors | Reserve success, warning, and risk colors for their intended meaning |
| Lines and shapes | Prefer flat forms, fine lines, restrained corner radii, and visually centered icons |

Avoid:

- Rainbow card cycles and continuous colored headings
- Large saturated areas, heavy borders, or decoration that competes with content
- Shrinking typography to fit excessive copy
- Meaningless flow nodes, glow effects, 3D robots, and nonfunctional controls
- Treating AI recommendations, user confirmation, platform execution, and business outcomes as the same state

### Project Structure

```text
product-solution-brief/
├── SKILL.md                         # Skill entry point and AI workflow
├── agents/
│   └── openai.yaml                  # Display metadata and default prompt
├── assets/
│   └── preview.png                  # Project preview
├── references/
│   ├── narrative-and-layout.md      # Narrative, theme, and visual-review rules
│   ├── page-brief.md                # Page brief and production-instruction framework
│   ├── layout-map.jpg               # Reference deck thumbnail map
│   └── reference.pdf                # Optional narrative and layout reference
└── scripts/
    ├── reference_pages.py           # Optional reference-page extraction
    └── assemble_pdf.py              # Optional ordered image-to-PDF assembly
```

The reference PDF is a narrative and layout example only. It is not a mandatory visual baseline, and its branding, cases, colors, and business capabilities must not be inherited by new projects.

### Optional Scripts

Scripts are utilities, not the skill's required entry point.

Dependencies:

```bash
python -m pip install PyMuPDF
```

Extract selected reference pages:

```bash
python scripts/reference_pages.py \
  --pages 1,3,4,5,14 \
  --output-dir /absolute/path/reference-pages
```

Assemble same-ratio page images into a PDF:

```bash
python scripts/assemble_pdf.py \
  --output /absolute/path/product-solution.pdf \
  /absolute/path/page-01.png \
  /absolute/path/page-02.png
```

Existing files are not overwritten by default. Add `--overwrite` explicitly only when replacement is intended.

### Quality Standards

Before delivery, verify that:

- Every page has one conclusion-led title and one clear focus
- Diagrams accurately represent objects, direction, responsibilities, and states
- Chinese text, numbers, dates, arrows, and case conditions remain consistent
- No glyphs are missing and no content is clipped, overlapping, awkwardly wrapped, or visually misaligned
- The primary color is coherent, supporting colors have clear roles, and risk colors are used only for risk
- Final PDF page count, order, aspect ratio, and clarity match the reviewed pages
- Full-page raster images are never described as editable source files

### Contributing

Contributions that improve narrative methods, business visual guidance, page briefs, and quality review are welcome. Before submitting, validate resource references, script syntax, and skill structure. Do not include temporary production files or unrelated logs.

---

<a id="中文文档"></a>
## 中文文档

### 目录

- [项目简介](#项目简介)
- [核心能力](#核心能力)
- [适用场景](#适用场景)
- [安装](#安装)
- [使用示例](#使用示例)
- [AI 工作流程](#ai-工作流程)
- [商务视觉原则](#商务视觉原则)
- [项目结构](#项目结构)
- [可选脚本](#可选脚本)
- [质量标准](#质量标准)
- [贡献](#贡献)

### 项目简介

ProductNarrative AI 帮助 AI 将产品资料转化为叙事清楚、图解准确、适合正式汇报的产品方案与 PDF。

技能遵循三项原则：

1. **叙事先于版式。** 先明确受众、决策场景、核心主张和页面逻辑，再开始设计。
2. **主题由内容决定。** 根据行业、品牌、受众和展示环境选择专业视觉主题，不强制使用固定红色或蓝色模板。
3. **检查真实交付文件。** 对最终 PDF 检查事实一致性、可读性、版式完整性和视觉克制程度。

### 核心能力

- **AI 主导设计**：由 AI 判断受众、沟通目标、叙事结构、图形形式和制作路线。
- **结论先行的叙事**：围绕为什么做、如何成立、谁负责、怎样达到结果以及创造什么价值组织内容。
- **可选择的商务主题**：将画布、表面、主色、字体、辅助色、语义色、线条、图标与留白定义为统一系统。
- **有明确用途的图解**：根据信息选择关系图、业务闭环、职责图、状态流程、对比表和案例故事板，而不是机械套用。
- **不绑定制作工具**：支持原生排版、矢量绘图、演示文稿、PDF 工作流和图像生成，脚本仅作为可选工具。
- **内置质量评审**：检查中文、数字、箭头、图标对齐、表格布局、跨页一致性和最终 PDF 完整性。

### 适用场景

推荐用于：

- 产品概念与产品方案汇报
- 管理层、投资人或客户决策材料
- 产品闭环、用户旅程与相关方职责说明
- AI 能力边界与人机责任分工
- 竞品能力映射与产品差异化表达
- 复杂业务方案的图解型 PDF

不适用于：

- 详细技术实现架构或接口设计
- 财务模型
- 日常文字润色
- 独立海报或营销长图

### 安装

#### 方式一：加入 Agent 技能目录

使用内部技能标识作为目录名克隆仓库：

```bash
git clone https://github.com/lengfengng-tech/product-narrative-ai.git product-solution-brief
```

将完整的 `product-solution-brief` 目录复制到 Agent 使用的技能目录，并确保当前环境能够发现 `SKILL.md`。

#### 方式二：构建 `.skill` 安装包

在 `product-solution-brief` 的上一级目录执行：

```bash
zip -r product-solution-brief.skill product-solution-brief \
  -x '*/__pycache__/*' '*.DS_Store'
```

通过支持 `.skill` 文件的客户端导入 `product-solution-brief.skill`。

### 使用示例

#### 生成管理层产品方案

```text
使用 product-solution-brief，根据当前项目资料制作一份管理层产品方案 PDF。
先判断受众与核心主张，再设计叙事和页面图解。
视觉采用专业克制的商务风，主题由你根据内容自主选择。
```

#### 指定品牌色

```text
使用 product-solution-brief 制作产品概念汇报。
保留企业品牌蓝作为主色，以白色和中性灰为主，辅助色只用于分类与状态。
先讲产品整体逻辑，再用一个连贯案例说明用户如何达到结果。
```

#### 只输出内容骨架

```text
使用 product-solution-brief 的叙事方法，先输出产品方案大纲。
每页给出结论标题、需要回答的问题和建议主视觉，暂不制作 PDF。
```

#### 评审现有方案

```text
使用 product-solution-brief 评审这份产品方案。
重点检查叙事是否结论先行、颜色是否喧宾夺主、图形是否准确表达业务关系，以及后半部分是否出现风格不一致或过度装饰。
```

### AI 工作流程

1. **判断任务**：识别受众、沟通目标、使用场景与期望动作。
2. **整理事实**：区分已确认事实、目标设计、示例数据、外部信息与待确认问题。
3. **设计叙事**：确定核心主张和页面顺序，每页只表达一个结论。
4. **定义视觉主题**：明确画布、表面、主色、正文、辅助色、语义色、字体、线条、图标与留白。
5. **选择合适图形**：让图形准确对应信息关系。
6. **制作与评审**：先检查封面、最复杂图解页和信息最密集页，再完成整套。
7. **核验交付文件**：重新打开最终 PDF，检查页序、比例、清晰度、文字与图形。

### 商务视觉原则

专业不等于单调，统一也不意味着每页都采用相同颜色处理。每种颜色都必须有明确职责。

| 视觉角色 | 使用原则 |
| --- | --- |
| 画布与表面 | 白色或中性色承担主要面积，保证投影与阅读对比 |
| 主色 | 用于品牌、当前重点和关键路径，避免铺满所有模块 |
| 正文 | 使用高对比深色，说明文字采用可读的中性灰 |
| 辅助色 | 通常 1–2 种，只用于稳定分类或相关方识别 |
| 语义色 | 成功、警告、风险按语义使用，不作普通装饰 |
| 线条与形状 | 平面、细线、适度圆角，图标保持视觉居中 |

应避免：

- 彩虹式卡片循环与连续彩色标题
- 大面积艳色、厚重边框或与内容争抢注意力的装饰
- 为塞入过多文字不断缩小字体
- 无意义流程节点、炫光、3D 机器人和不可用的假控件
- 把 AI 建议、用户确认、平台执行和业务结果混为同一状态

### 项目结构

```text
product-solution-brief/
├── SKILL.md                         # 技能入口与 AI 工作流
├── agents/
│   └── openai.yaml                  # 展示信息与默认提示词
├── assets/
│   └── preview.png                  # 项目预览图
├── references/
│   ├── narrative-and-layout.md      # 叙事、主题与视觉评审规则
│   ├── page-brief.md                # 单页简报与制作指令框架
│   ├── layout-map.jpg               # 参考稿版式缩略图
│   └── reference.pdf                # 可选叙事与版式参考
└── scripts/
    ├── reference_pages.py           # 可选：提取参考 PDF 页面
    └── assemble_pdf.py              # 可选：按顺序合成页图 PDF
```

参考 PDF 仅作为叙事与版式案例，不是强制视觉基准。新项目不得继承其中的品牌、案例、配色或业务能力。

### 可选脚本

脚本是辅助工具，不是技能的固定入口。

依赖安装：

```bash
python -m pip install PyMuPDF
```

提取指定参考页：

```bash
python scripts/reference_pages.py \
  --pages 1,3,4,5,14 \
  --output-dir /absolute/path/reference-pages
```

将同比例页图合成为 PDF：

```bash
python scripts/assemble_pdf.py \
  --output /absolute/path/product-solution.pdf \
  /absolute/path/page-01.png \
  /absolute/path/page-02.png
```

默认不覆盖已有文件。确需替换合成结果时，明确添加 `--overwrite`。

### 质量标准

交付前至少确认：

- 每页只有一个结论式标题和一个清晰焦点
- 图形准确表达对象、方向、职责与状态
- 中文、数字、日期、箭头和案例条件前后一致
- 没有缺字、截断、重叠、异常换行或视觉偏心
- 主色统一，辅助色职责明确，风险色只用于风险
- 最终 PDF 的页数、页序、比例和清晰度与已检查页面一致
- 不将整页位图描述为可编辑源文件

### 贡献

欢迎提交针对叙事方法、商务视觉规则、单页简报和质量评审的改进。提交前请检查资源引用、脚本语法与技能结构，不要加入临时制作文件或无关日志。
