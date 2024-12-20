"""
增强问题质量

1. 找到问题中模糊描述，给出更具体提问的例子。
2. 分析问题所涉及的领域，可能会让这个问题的背景更清晰。
3. 分析历史，是不是历史上也有过人做出类似的提问。有没有类似的尝试，可以提供参考。

"""

class EnhanceQ:
    def __init__(self, question: str):
        self.rawQuestion = question
        self.question = question

    def concretize(self):
        self.question = f"\"{self.question}\"\n我现在有一个这样的模糊概念，但是这个问题不够具体，可以帮我改善一下吗"
    
    def getDomain(self):
        self.question = f"{self.question}\n我想问的核心概念是什么，这个是什么领域的问题。可以给出针对这个领域的问题详细描述吗"
    
    def getHistory(self):
        self.question = f"{self.question}\n历史上有没有人问过类似的问题，可以提供参考吗"

    def enhanceV1(self):
        self.concretize()
        self.getDomain()
        self.getHistory()
        return self.packUp()
    def packUp(self):
        pack = [
            {
                "role": "system",
                "content": "你是一个分析问题的专家，比起给出答案，你更擅长分析问题，并给出更具体的问题。请你真对我的问题给出更多的提问方式启发我。回答的最后，给我一个可以选填的问题框架"
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
