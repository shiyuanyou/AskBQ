from pywebio.input import input
from pywebio.output import (
    put_markdown,
    clear,
    put_text,
    put_loading,
    OutputPosition,
    put_scrollable
)
import time

def loopInputExcute(func):
    while True:
        user_input = input("请输入内容：")
        if user_input == "exit":
            break

        put_text("请等待", 'info')
        put_loading(shape='border', color='info')
        result = func(user_input)
        clear()
        put_markdown(f"# 问题\n ## {user_input}")  
        put_scrollable(
            put_markdown(f"# 输出\n ## {result}"),
            height=500,
            keep_bottom=True
        )


def foo(x:str):
    time.sleep(2)
    ret = f"xxx\n ## 您输入的内容是\n{x*100}\n ## 您输入的内容是\n{x*100}"
    return ret

def main():
    loopInputExcute(foo)

if __name__ == '__main__':
    main()
