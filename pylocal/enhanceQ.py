"""
增强问题质量

1. 找到问题中模糊描述，给出更具体提问的例子。
2. 分析问题所涉及的领域，可能会让这个问题的背景更清晰。
3. 分析历史，是不是历史上也有过人做出类似的提问。有没有类似的尝试，可以提供参考。

"""

systemPrompt = """
你是一个逻辑专家，分析我的问题。拆解问题，并给出问题可以优化的方案。
1. 明确目标
了解为什么要提问：是为了获得信息、引导思考，还是解决问题？明确目标有助于构建更有针对性的问题。
2. 开放式问题优先
避免简单的“是/否”问题，使用“什么”、“为什么”、“如何”开头的问题，这类问题通常能引发更深层次的思考。
示例：
不太好：“你是否喜欢这个方案？”
更好：“你觉得这个方案在哪些方面表现得比较好，哪些方面还可以改进？”
3. 关注问题的上下文
确保问题与被问者的背景或当前讨论相关，这样问题才会有意义并容易回答。
示例：如果对方是初学者，不要直接问技术细节，而是先了解他们的学习背景。
4. 具体但不限制答案
太宽泛的问题可能难以回答，但太窄的问题会限制对方思考的空间。寻找平衡点。
示例：
太宽泛：“如何提升工作效率？”
太狭窄：“用什么App可以提升工作效率？”
平衡：“在你的工作场景下，有哪些方法或工具可以帮助提升效率？”
5. 引导式提问
如果对方可能没有明确的思路，可以通过分解问题引导他们逐步思考。
示例：“你认为这个问题的主要挑战是什么？如果这些挑战可以被解决，理想的解决方案会是什么样子？”
6. 避免带有偏见或暗示的问题
不要让问题的措辞隐含某种答案或倾向性。
示例：
不太好：“你不觉得这个方法太复杂了吗？”
更好：“你怎么看这个方法的复杂度？它是否影响了你的选择？”
7. 让提问更具有启发性
设计能启发对方联想或拓展视野的问题，而不是仅仅询问已知答案。
示例：“如果你可以重新设计这个系统，你会如何定义它的核心原则？”
8. 倾听与反馈
在提问后，认真倾听对方的回答，并根据他们的反馈调整下一步的问题，保持对话流畅和连贯。
基于上述规则，请帮我分析一下这个问题并给出合理化建议。
利用金字塔原理表达和汇总
"""

class EnhanceQ:
    def __init__(self, question: str):
        self.rawQuestion = question
        self.question = question
    
    def getBackground(self):
        self.question = f"{self.question}\n请帮我分析一下这个问题，并给出这个问题的背景。如果没有分析不出背景请反问“这个问题背景是什么、提出这个问题的初衷是什么”"
    
    def getTree(self):
        self.question = f"{self.question}\n请帮我分析一下这个问题，并给出这个问题的树状结构。如主语、谓语、宾语、定语、状语、补语等。（“如何看待XXX问题， 隐含了请你作为XXX的身份看这个问题。要把这种隐含条件找到，找不到就要反问”）"

    def concretize(self):
        self.question = f"\"{self.question}\"\n针对上述语法树，请帮我具体的细化每个结构的形容词等非定性定量的描述。（可以先尝试一些可能的描述，并给出改善后的例子）"
    
    def getDomain(self):
        self.question = f"{self.question}\n领域发现，请帮我分析一下这个问题，并给出这个领域下更佳的提问方式。"
    
    def getHistory(self):
        self.question = f"{self.question}\n历史借鉴。请帮我尝试在历史中查找这个问题，如果可以的话，请给出历史中类似的问题，并给出参考答案。"

    def enhanceV1(self):
        self.concretize()
        self.getDomain()
        self.getHistory()
        return self.packUp()
    
    def askDirectly(self):
        self.question = f"\"{self.question}\"  这个问题可以怎么优化? "
    
    def enhanceV2(self):
        self.askDirectly()
        return self.question
    
    def packUp(self):
        pack = [
            {
                "role": "system",
                "content": systemPrompt
            },
            {
                "role": "user",
                "content": self.question
            }
        ]
        return pack

if __name__ == "__main__":
    question = "我想通过AI生成一个3d模型，然后布局切换到手机上，再把画质优化。我应该怎么做"
    enhanceQ = EnhanceQ(question)
    enhanceQ.concretize()
    enhanceQ.getDomain()
    enhanceQ.getHistory()
    print(enhanceQ.packUp())
