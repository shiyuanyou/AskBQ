from pywebio.input import input
from pywebio.output import (
    put_markdown,
    clear,
    put_text
)
import time

def loopInputExcute(func):
    while True:
        user_input = input("请输入内容：")
        if user_input == "exit":
            break
        put_text("请稍等，正在处理...").style('color: blue; font-size: 18px;')

        result = func(user_input)
        clear()
        put_markdown(f"# 问题\n ## {user_input}")
        put_markdown(result)

def foo(x:str):
    time.sleep(5)
    ret = f"# 输出\n ## 您输入的内容是\n{x}"
    return ret

def main():
    loopInputExcute(foo)

if __name__ == '__main__':
    main()
