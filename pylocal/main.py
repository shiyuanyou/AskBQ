from openai import OpenAI
import argparse
import logging
import os
from datetime import datetime
import pytz

from encrypt import getKey
from errorCode import (
    RequestErrorCode,
    hintRequestErrorCode
)
from enhanceQ import EnhanceQ
from webView import loopInputExcute

# 设置日志配置
log_dir = "/workspaces/AskBQ/pylocal/log"
os.makedirs(log_dir, exist_ok=True)

# 创建自定义的时间格式器
class BeijingFormatter(logging.Formatter):
    def converter(self, timestamp):
        beijing_tz = pytz.timezone('Asia/Shanghai')
        return datetime.fromtimestamp(timestamp, beijing_tz)
    
    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            return dt.strftime(datefmt)
        return dt.strftime('%Y-%m-%d %H:%M:%S')

# 配置日志
formatter = BeijingFormatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler(f"{log_dir}/app.log")
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

url = "https://api.deepseek.com"

def getResult(client, messages):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            # response_format={ 'type': 'json_object' },
            stream=False
        )
    except Exception as e:
        error_code = e.code
        logging.error(f"Error code: {error_code}")
        # logging.error(f"Error message: {hintRequestErrorCode[error_code]}") 
        logging.error(f"Error creating OpenAI client: {e}")
        return ""
    return response.choices[0].message.content

def main(rawQuestion:str):
    key = getKey()
    try:
        client = OpenAI(api_key=key, base_url=url)
    except Exception as e:
        logging.error(f"Error creating OpenAI client: {e}")
        return
    
    enhanceQ = EnhanceQ(rawQuestion)
    messages = enhanceQ.enhanceV1()
    logging.info(messages)
    result = getResult(client, messages)
    logging.info("-" * 35)
    
    logging.info(f"rawQuestion: {rawQuestion}")
    logging.info(result)
    
    logging.info("-" * 35)
    return result

if __name__ == "__main__":
    loopInputExcute(main)
