# 核心概念：如何优化问题

## 总结（懒人省流版）

为什么有不好的问题：
1. 第一，第一直觉懒。不是不会，但是直接想到哪说到哪
2. 第二，没有陌生领域。完全不知道该问什么
3. 第三，没有逻辑能力差。不知道怎么问，自己前后都矛盾

解决这三类问题，就是让人多问几下，引导用户。对于我自己，经常是第二点和第一点（不想承认是第三点）。

## 蠢问题

可能有些人还没有读过非常知名的《提问的艺术》：[提问的艺术](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)

但是这里有一个非常有趣的前提，提问前要做好准备：
> 在你准备要通过电子邮件、新闻群组或者聊天室提出技术问题前，请先做到以下事情：
>   - 尝试在你准备提问的论坛的旧文章中搜索答案。
>   - 尝试上网搜索以找到答案。
>   - 尝试阅读手册以找到答案。
>   - 尝试阅读常见问题文件（FAQ）以找到答案。
>   - 尝试自己检查或试验以找到答案。
>   - 向你身边的强者朋友打听以找到答案。
>   - 如果你是程序开发者，请尝试阅读源代码以找到答案。

读书和工作的时候，笔者经常被蠢问题烦到，所以提问的时候经常会先去做好各种准备工作再去提问。在没有大模型的时代简直折磨，因为往往准备工作就要比解决问题要旧很多。很多时候会浪费大量时间，还不如直接提问。然后有经验的老师傅会帮你优化方向，让你聚焦于某些地方，就可以解决问题了。

本项目有了3个核心目标：
1. 检查是不是好问题
2. 问题是不是可以拆解
3. 提问者的本意是什么，是不是真的要回答问题，提问本身是不是因为其他问题导致。那帮提问者找到自己真的疑惑的事情是不是就可以了

## 模糊描述

Q: 我想通过AI生成一个3d模型，然后布局切换到手机上，再把画质优化。我应该怎么做

模糊描述
1. 什么样的3d模型
2. 什么叫切换到手机上
3. 是全平台都要做吗？（安卓、鸿蒙next、iphone）
4. 画质优化，是具体那些方面
   1. 清晰度？
   2. 分辨率？
5. 优化到什么程度
   1. 不再是马赛克
   2. 有锐利清晰的边缘
   3. 以假乱真

以此基准，重新看三个目标：
> 本项目有了3个核心目标：
> 1. 检查是不是好问题
> 2. 问题是不是可以拆解
> 3. 提问者的本意是什么，是不是真的要回答问题，提问本身是不是因为其他问题导致。那帮提问者找到自己真的疑惑的事情是不是就可以了

1. 什么是好问题？
2. 拆解要到什么粒度？
3. 如何知道提问者的本意？

## step1 直接优化

### 问答

#### 问答1

“我想通过AI生成一个3d模型，然后布局切换到手机上，再把画质优化。我应该怎么做”。

我现在有一个这样的模糊概念，但是这个问题可能不够好，不够具体，可以帮我改善一下吗

##### 答

>这是一个有趣的想法！为了让问题更具体并且易于执行，可以从以下几个方面着手澄清和完善你的问题： 
>
>1. **目的与场景**
>- 你希望生成的3D模型是什么？比如，是人物、建筑、还是某种艺术品？  
>- 在布局切换到手机上时，主要目标是什么？是为了实时展示，还是为了后期编辑或使用？  
>- 优化画质是为了增强渲染效果、提高用户体验，还是为了在性能和效果之间找到平衡？  
>
>2. **技术路径与限制**
>- 你是否已经有相关的技术栈或工具，比如 3D 建模软件（Blender、Maya）、渲染引擎（Unity、Unreal Engine），以及 AI 模型生成工具（如 Stable Diffusion 3D 模型插件）？  
>- 手机设备的性能限制需要考虑吗？特别是低端设备和高端设备之间的兼容性。  
>
>3. **期望输出**
>- 对最终的模型画质有什么具体要求？例如，是否需要支持 PBR 材质、光影效果？分辨率和帧率有没有要求？  
>- 是否需要用户能够交互，比如旋转、缩放模型，或者改变某些参数？  
>
>基于这些澄清，问题可以重新表述如下： 
>
>> "我希望通过 AI 工具生成一个特定类型的 3D 模型（如人物、建筑等），然后将该模型适配到手机端应用展示，支持实时交互，同时在画质优化方面能在性能和视觉效果之间找到平衡。针对这个目标，我需要明确以下几点：  
>> 1. 选择合适的 3D 模型生成和优化工具链。  
>> 2. 如何高效地将模型从生成工具转换为适配移动端的格式（如 glTF、USDZ）。  
>> 3. 在手机端实现实时渲染的最佳实践（如使用 WebGL 或 Unity Mobile）。  
>> 4. 有哪些方法可以进一步优化模型画质，同时兼顾性能？"  
>
>你觉得这个改进版本符合你的需求吗？如果有其他细节，我们可以进一步调整！

#### 问答2

“为什么最近孩子成绩下降了？”我现在有一个这样的疑惑，请帮我优化一些这个问题，我觉得这个问题还不够好

##### 答

> 当然，优化问题可以帮助我们更深入地理解孩子成绩下降的原因。以下是一些改进后的问题，它们可以帮助你更全面地分析情况：
> 
> 1. **成绩下降的时间范围**：
>    - “孩子的成绩是从什么时候开始下降的？”
> 
> 2. **成绩下降的科目**：
>    - “孩子的成绩是在所有科目中都有所下降，还是只在某些特定科目？”
> 
> 3. **学习态度和行为**：
>    - “孩子最近在学习态度或行为上有什么变化吗？”
> 
> 4. **家庭和学校环境**：
>    - “家庭环境或学校环境最近有没有发生什么变化，可能会影响孩子的学习？”
> 
> 5. **个人健康和情绪**：
>    - “孩子最近有没有健康问题或情绪波动，这可能影响了他的学习？”
> 
> 6. **学习策略和方法**：
>    - “孩子是否尝试了新的学习方法或策略，但效果不佳？”
> 
> 7. **课外活动和压力**：
>    - “孩子是否参与了更多的课外活动，这可能分散了他对学习的注意力？”
> 
> 8. **教师和同学的影响**：
>    - “孩子是否受到了老师或同学的负面影响？”
> 
> 9. **目标和动机**：
>    - “孩子是否有明确的学习目标和动机？”
> 
> 10. **家庭支持和期望**：
>     - “家庭是否提供了足够的支持和合理的期望，以帮助孩子保持学习动力？”
> 
> 通过这些问题，你可以更系统地探索孩子成绩下降的潜在原因，并采取相应的措施来帮助他们。


### 对比kimi的插件 “费曼学习法”

> 🌟 **Why：与我何干？**
> 成绩下降对每个孩子和家长来说都是很重要的问题，因为它可能影响到孩子的自信心、未来的学习机会以及家庭的期望。了解成绩下降的原因可以帮助我们找到解决问题的方法，从而帮助孩子回到正轨。
> 
> 📚 **What：定义、概念解释，可以做什么**
> 成绩下降指的是孩子在一段时间内，学业成绩相比之前有所下滑。这可能是由多种因素引起的，比如学习习惯的改变、家庭环境的影响、心理压力的增加等。了解这些因素可以帮助我们采取相应的措施。
> 
> 🛠️ **How：步骤流程方法，以及解释所需的任何主题内容。包括举例子、打比方等。**
> 1. **观察和沟通**：首先，观察孩子的行为变化，与孩子进行开放和非指责性的对话，了解他们的感受和遇到的问题。
> 2. **分析原因**：可能的原因包括学习压力、家庭问题、健康问题、社交问题等。比如，如果孩子最近经常熬夜，可能是因为他们在晚上花了很多时间玩游戏或上网，导致睡眠不足，影响第二天的学习效率。
> 3. **制定计划**：根据分析的原因，制定一个改善计划。比如，如果是因为学习时间管理不当，可以一起制定一个合理的学习计划，包括休息和娱乐时间。
> 4. **寻求帮助**：如果问题比较复杂，比如涉及到心理健康，可能需要寻求专业人士的帮助。
> 
> 🏆 **How good：可以给听众带来什么好处，什么改变。**
> 通过解决成绩下降的问题，孩子可以恢复学习动力，提高学习效率，增强自信心，同时也能改善家庭关系。长远来看，这对孩子的个人发展和未来的教育及职业道路都是有益的。
> 
> 是否需要调整难度等级？如果内容太复杂，输入'-'返回更简单的笔记；如果内容太简单，输入'+'返回更详细的笔记。

这种假模假样的给了WH组合，其实根本不触达核心。

## step2 领域优化

### 问答case

“我的孩子最近成绩下降了，我想知道原因”

我现在有一个这样的模糊概念，但是这个问题可能不够好，不够具体，可以帮我改善一下吗。
我想问的核心概念是什么，这个是什么领域的问题。可以给出针对这个领域的问题详细描述吗

#### 答案

> 核心概念：
> 1. 学习动机与表现：孩子的学习动机、学习习惯以及他们在学校的表现之间的关系。
> 2. 家庭教育与支持：家庭环境、家长的教育方式以及这些因素如何影响孩子的学习成绩。
> 3. 心理健康与压力管理：孩子的情绪状态、压力水平以及这些因素如何影响他们的学习表现。
> 
> 改进后的问题描述：
> 1. 学习动机与习惯：“我的孩子最近成绩下降了，我想知道是否与他们的学习动机或学习习惯有关。具体来说，他们是否对学习失去了兴趣？他们的学习时间管理是否合理？是否有足够的时间用于复习和完成作业？”
> 2. 家庭教育与支持：“我的孩子最近成绩下降了，我想知道是否与家庭环境或我的教育方式有关。具体来说，我是否提供了足够的学习支持？我是否在孩子的学习过程中给予了适当的鼓励和反馈？家庭中的其他因素（如家庭氛围、兄弟姐妹的影响）是否影响了他们的学习？”
> 3. 心理健康与压力管理：“我的孩子最近成绩下降了，我想知道是否与他们的情绪状态或压力水平有关。具体来说，他们是否感到过度焦虑或压力？是否有其他心理健康问题（如抑郁、注意力缺陷）影响了他们的学习表现？我该如何帮助他们管理这些情绪和压力？”
> 
> 针对这个领域的详细问题描述：
> 1. 学习动机与表现：“我的孩子最近成绩下降了，我想了解他们的学习动机是否发生了变化。他们是否对某些科目失去了兴趣？是否有特定的学习习惯（如拖延、不按时完成作业）导致了成绩下降？我该如何帮助他们重新激发学习兴趣并改善学习习惯？”
> 2. 家庭教育与支持：“我的孩子最近成绩下降了，我想了解家庭环境是否对他们的学习产生了负面影响。我是否在孩子的学习过程中提供了足够的支持？我是否在他们的学习过程中给予了适当的鼓励和反馈？家庭中的其他因素（如家庭氛围、兄弟姐妹的影响）是否影响了他们的学习？我该如何调整我的教育方式以更好地支持他们的学习？”
> 3. 心理健康与压力管理：“我的孩子最近成绩下降了，我想了解他们的情绪状态和压力水平是否影响了他们的学习表现。他们是否感到过度焦虑或压力？是否有其他心理健康问题（如抑郁、注意力缺陷）影响了他们的学习表现？我该如何帮助他们管理这些情绪和压力，以改善他们的学习表现？”


