#coding:utf-8

from config import auConfigs
from controller import auController
from telegram.ext import Updater

# 引入设置文件
configs = auConfigs()

def main():
    updater = Updater(configs.get_token(),use_context=True,request_kwargs=configs.proxy)
    dispatcher = updater.dispatcher
    auController(dispatcher=dispatcher,config=configs)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()





