from aip import AipSpeech
import time
import logging
import subprocess
import cv2
import paddlehub as hub
import numpy as np
import shutil
import os

class picToanime:

    def __init__(self,chat_id,pic,config,query,style):
        self.chat_id = chat_id
        self.configs = config
        self.logger = logging.getLogger("Pic_to_Anime Log")
        self.pic = pic
        self.query = query
        self.style = style

    def savePicture(self,pic):
        picname = '{}-{}.{}'.format(self.chat_id, int(time.time()), pic.file_path.split('.')[-1])
        # 将文件保存到地址 voice中
        picpath = '{}/{}/{}'.format('trash','AnimeGAN', picname)
        # 下载文件
        with open(picpath, 'wb') as f:
            pic.download(out=f)
        self.query.edit_message_text('保存完成！✅')
        return picpath

    def convertPicture(self,picpath):
        self.query.edit_message_text('转换中……（时间较长，耐心等待；转换失败，返回404）')
        if(self.style=='1'):
            model = hub.Module(name='animegan_v2_hayao_64', use_gpu=True)
        elif(self.style=='2'):
            model = hub.Module(name='animegan_v2_shinkai_53', use_gpu=True)
        elif(self.style=='3'):
            model = hub.Module(name='animegan_v2_paprika_97', use_gpu=True)
        else:
            model = hub.Module(name='animegan_v2_hayao_64', use_gpu=True)
        if not os.path.exists('trash/AnimeGAN/Result'):
            os.mkdir('trash/AnimeGAN/Result')
        shutil.rmtree('trash/AnimeGAN/Result')
        result = model.style_transfer(images=[cv2.imread(picpath)], visualization=True,
                                      output_dir='trash/AnimeGAN/Result')

    def run(self):
        picpath = self.savePicture(self.pic)
        self.convertPicture(picpath)
        filename = os.listdir("trash/AnimeGAN/Result")[0]
        photo = '{}/{}/{}/{}'.format('trash','AnimeGAN','Result',filename)
        return photo

