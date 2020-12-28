from telegram.ext import CommandHandler, MessageHandler, Filters,CallbackQueryHandler,CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from app.voiceTotext import voiceTotext
from app.picToanime import picToanime
from app.getHitokoto import getHitokoto
from app.getQrcode import getqrcode
import logging
import time
import shutil
import os

class auController:

    def __init__(self,dispatcher,config):
        self.logger = logging.getLogger("auController")
        self.dp = dispatcher
        self.bot = self.dp.bot
        self.__controller()
        self.configs = config
        # self.pic = None

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
                                           '2. 待添加……'
        update.message.reply_text(reply_text)

    def voice(self,update,context):
        reply_text = '语音转文字\n可直接转发语音至au机器人\n目前只支持中文语音转文字\n语音的时间尽可能控制在30s左右\n使用百度api接口转换\n' \
                     '如遇翻译不准确，本人学艺不精，无法修正'
        update.message.reply_text(reply_text)

    def trash(self,update,context):
        reply_text = '非法指令！❌'
        if update.effective_chat.id == self.configs.admin_chat_id:
            shutil.rmtree('trash')
            os.makedirs('trash/voice')
            os.makedirs('trash/AnimeGAN')
            os.makedirs('trash/qrcode')
            reply_text = '垃圾清理完成！✅'

        update.message.reply_text(reply_text)


    # 用户交流 复读用户发送消息 或者 其他
    def echo(self,update,context):
        text = update.message.text
        reply_text = text
        if(text == 'hsh' and update.message.from_user['id']==self.configs.hsh_chat_id):
            reply_text = "你好，shihua，很高兴认识你。"
        elif(text == 'au'):
            reply_text = "叫我干嘛？你au爹不会给你做牛做马的，哼~"
        update.message.reply_text(reply_text)

    # 语音转文字 baidu api接口
    def voice_to_text(self,update,context):
        if (self.configs.voiceTotext == 0):
            return update.message.reply_text('语音转文字 - 暂时关闭')
        self.user_id = update.message.from_user['id']
        voice = context.bot.get_file(update.message.voice)
        firstText = update.message.reply_text('转换中……')
        text = voiceTotext(update.message.from_user['id'], voice, self.configs).run()
        keyboard = [[InlineKeyboardButton(text="Forward", url='https://t.me/share/url?url='+text)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        firstText.edit_text(text,reply_markup=reply_markup)

    # 图片动漫风格化
    def picture_to_anime(self,update,context):
        if(self.configs.picToanime==0):
            return update.message.reply_text('图片动漫风格化 - 暂时关闭')
        # pic = context.bot.get_file(update.message.photo[-1].file_id)
        self.pic_id = update.message.photo[-1].file_id
        self.user_id = update.message.from_user['id']
        keyboard = [
            [
                InlineKeyboardButton("宫崎骏", callback_data='1'),
                InlineKeyboardButton("新海诚", callback_data='2'),
            ],
            [
                InlineKeyboardButton("今敏红辣椒", callback_data='3'),
                InlineKeyboardButton("取消", callback_data='4'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('选择你需要的风格:', reply_markup=reply_markup)
        # firstText = update.message.reply_text('图片保存中……（时间较长，耐心等待；保存失败，返回404）')
        # photo = picToanime(update.message.from_user['id'],pic,self.configs,firstText).run()
        # update.message.reply_photo(open(photo,'rb'))
        # firstText.edit_text('转换完成！✅')

    def picture_to_anime_button(self,update,context):
        query = update.callback_query
        query.answer()
        if (query.data != '4'):
            query.edit_message_text(text=f"图片保存中……（时间较长，耐心等待；保存失败，返回404")
            pic = context.bot.get_file(self.pic_id)
            photo = picToanime(self.user_id,pic, self.configs, query,query.data).run()
            self.bot.send_photo(chat_id=self.user_id, photo=open(photo,'rb'))
        else:
            query.edit_message_text(text=f"祝你快乐！")

    # 一言名言
    def get_hitokoto(self,update,context):
        if (self.configs.getHitokoto == 0):
            return update.message.reply_text('一言名言 - 暂时关闭')
        update.message.reply_text(getHitokoto().run())

    # 文本qrcode
    def get_qrcode(self,update,context):
        if (self.configs.getQrcode == 0):
            return update.message.reply_text('文字转二维码 - 暂时关闭')
        reply_text = '文本二维码\n' \
                     '/qr [文本]\n' \
                     '例: /qr 123'
        if (len(context.args) != 0):
            content = ''
            for arg in context.args:
                content = content+' '+arg
            content.strip(' ')
            photo = getqrcode(content, update.message.from_user['id'])
            self.bot.send_photo(chat_id=update.message.from_user['id'], photo=open(photo, 'rb'))
            # update.message.reply_text(content)
        else:
            update.message.reply_text(reply_text)

    def error(self,update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)
        update.message.reply_text("404")
        # self.bot.send_message(chat_id=self.user_id, text="I'm sorry Dave I'm afraid I can't do that.")

    # 添加至调度器
    def __controller(self):

        handlers = []

        # 添加顺序代表了 优先级
        handlers.append(CommandHandler('start',self.start))
        handlers.append(CommandHandler('hsh',self.hsh))
        handlers.append(CommandHandler('help', self.help))
        handlers.append(CommandHandler('voice',self.voice))
        handlers.append(CommandHandler('trash', self.trash))
        handlers.append(CommandHandler('quoto',self.get_hitokoto))
        handlers.append(CommandHandler('qr',self.get_qrcode))
        handlers.append(MessageHandler(Filters.text,self.echo))
        handlers.append(MessageHandler(Filters.voice,self.voice_to_text))
        handlers.append(MessageHandler(Filters.photo, self.picture_to_anime))
        handlers.append(CallbackQueryHandler(self.picture_to_anime_button))


        for handler in handlers:
            self.dp.add_handler(handler)

        self.dp.add_error_handler(self.error)


