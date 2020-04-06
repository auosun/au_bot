#coding:utf-8

from config import auConfigs
from controller import auController
from telegram.ext import Updater
import logging
# 引入设置文件
configs = auConfigs()

if(configs.status):
    logging.basicConfig(filename='au_bot.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
else:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def main():
    updater = Updater(configs.get_token(),use_context=True,request_kwargs=configs.proxy)
    dispatcher = updater.dispatcher
    auController(dispatcher=dispatcher,config=configs)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()





