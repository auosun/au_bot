#coding:utf-8
import os
from config.config import auConfigs
from controller import auController
from telegram.ext import Updater
import logging
# 引入设置文件
configs = auConfigs()

def main():
    if not os.path.exists('voice'):
        os.makedirs('voice')
    updater = Updater(configs.get_token(),use_context=True,request_kwargs=configs.proxy)
    dispatcher = updater.dispatcher
    auController(dispatcher=dispatcher,config=configs)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
