from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from app.voiceTotext import voiceTotext
from app import getwzywords,getProxy,bindAccount
from v2ray_api.v2rayController import get_vmess
import logging
import time

class auController:

    def __init__(self,dispatcher,config):
        self.logger = logging.getLogger("auController")
        self.dp = dispatcher
        self.__controller()
        self.configs = config

    # 开始提示
    def start(self,update,context):
        # chat_id = update.effective_chat.id
        # print(update.effective_chat)
        update.message.reply_text("你好,我叫 Au\n/help 获取帮助，你会喜欢我的")

    # hsh彩蛋
    def hsh(self,update,context):
        chat_id = update.effective_chat.id
        reply_text = "你谁啊？整啥玩意儿就输 hsh啊！"
        if chat_id == self.configs.hsh_chat_id:
            reply_text = "Hi, ShiHua, Have a nice day!"
        update.message.reply_text(reply_text)

    # help帮助信息
    def help(self,update,context):
        reply_text = '你好，'+update.message.from_user['first_name']+'\n我是au,目前集成功能：\n' \
                                           '1. /voice 语音转文字\n' \
                                           '2. /proxy 代理分发\n' \
                                           '3. 待添加……'
        update.message.reply_text(reply_text)

    def voice(self,update,context):
        reply_text = '语音转文字\n可直接转发语音至au机器人\n目前只支持中文语音转文字\n语音的时间尽可能控制在30s左右\n使用百度api接口转换\n' \
                     '如遇翻译不准确，本人学艺不精，无法修正'
        update.message.reply_text(reply_text)

    def proxy(self,update,context):
        reply_text = '代理分发\n' \
                     '获取MTP代理，可发送 /proxy mtp\n' \
                     '获取其他协议代理请按一下格式输入：\n' \
                     '/proxy [password] [type]\n' \
                     'type可选参数:\n' \
                     'http socks v2ray switch ss mtp'
        if(len(context.args)):
            reply_text = getProxy.getProxy(context.args)
        update.message.reply_text(reply_text)

    # 用户交流 复读用户发送消息 或者 其他
    def echo(self,update,context):
        text = update.message.text
        reply_text = text
        if(text == 'hsh' and update.message.from_user['id']==self.configs.hsh_chat_id):
            reply_text = "你好，shihua，很高兴认识你。"
        elif(text == 'au'):
            reply_text = "叫我干嘛？你au爹不会给你做牛做马的，哼~"
        elif(text == '说骚话' and update.message.from_user['id'] == self.configs.wzy_chat_id):
            reply_text = getwzywords.getwzywords()
        update.message.reply_text(reply_text)

    # 语音转文字 baidu api接口
    def voice_to_text(self,update,context):
        voice = context.bot.get_file(update.message.voice)
        text = voiceTotext(update.message.from_user['id'], voice, self.configs).run()
        keyboard = [[InlineKeyboardButton(text="Forward", url='https://t.me/share/url?url='+text)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(text,reply_markup=reply_markup)

    def bind(self,update,context):
        reply_text = '绑定账户\n' \
                     '/bind [邮箱]\n' \
                     '例: /bind 123@qq.com'
        # print(update.message.from_user['id'])

        if (len(context.args)==1):
            reply_text = bindAccount.bindAccount(update.message.from_user,context.args[0])
            # print(update.message.from_user)
            # vmess_url = get_vmess(context.args[0])
        update.message.reply_text(reply_text)


    def link(self,update,context):
        vmess_url = get_vmess(update.message.from_user['id'])
        if(vmess_url):
            update.message.reply_text(vmess_url)
        else:
            update.message.reply_text('失败')


    def error(self,update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)
        update.message.reply_text("404")

    # 添加至调度器
    def __controller(self):

        handlers = []

        start_handler = CommandHandler('start',self.start)
        hsh_handler = CommandHandler('hsh',self.hsh)
        help_handler = CommandHandler('help', self.help)
        voice_handler = CommandHandler('voice',self.voice)
        proxy_handler = CommandHandler('proxy',self.proxy)
        bind_handler = CommandHandler('bind',self.bind)
        link_handler = CommandHandler('link',self.link)
        echo_handler = MessageHandler(Filters.text,self.echo)
        stt_handler = MessageHandler(Filters.voice,self.voice_to_text)


        # 添加顺序代表了 优先级
        handlers.append(start_handler)
        handlers.append(hsh_handler)
        handlers.append(help_handler)
        handlers.append(voice_handler)
        handlers.append(proxy_handler)
        handlers.append(bind_handler)
        handlers.append(link_handler)
        handlers.append(echo_handler)
        handlers.append(stt_handler)


        for handler in handlers:
            self.dp.add_handler(handler)

        self.dp.add_error_handler(self.error)


