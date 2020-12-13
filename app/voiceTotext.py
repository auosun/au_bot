from aip import AipSpeech
import time
import logging
import subprocess

class voiceTotext:

    def __init__(self,chat_id,voice,config):
        self.chat_id = chat_id
        self.configs = config
        self.client = AipSpeech(self.configs.BAIDU_VOICE_API_ID,self.configs.BAIDU_VOICE_API_KEY,self.configs.BAIDU_VOICE_SECRET_KEY)
        self.logger = logging.getLogger("Voive_to_text Log")
        self.ffmpeg = self.configs.ffmpeg
        self.voice = voice

    # 保存语音文件 并返回文件地址
    def saveVoice(self,voice):
        # 文件名格式为 < id > - < time >.oga
        voicename = '{}-{}.{}'.format(self.chat_id,int(time.time()),voice.file_path.split('.')[-1])
        # 将文件保存到地址 voice中
        voicepath = '{}/{}/{}'.format('trash','voice',voicename)
        # 下载文件
        with open(voicepath,'wb') as f:
            voice.download(out=f)
        # self.logger.info("download success "+voicename)
        return voicepath

    # oga转换wav
    def oga_to_wav(self,voicepath):
        wavname = '{}.{}'.format(voicepath.split('.')[0],'wav')
        ogatowav = self.ffmpeg+" -v quiet -i "+voicepath+" "+wavname
        subprocess.call(ogatowav, shell=True)
        # self.logger.info("oga to wav success "+ogatowav)
        return wavname

    # wav转换16k pcm
    def wav_to_pcm(self,wavpath):
        pcmname = '{}.{}'.format(wavpath.split('.')[0],'pcm')
        wavtopcm = self.ffmpeg+" -y -v quiet -i "+wavpath+" -acodec pcm_s16le -f s16le -ac 1 -ar 16000 "+pcmname
        subprocess.call(wavtopcm,shell=True)
        # self.logger.info("wav to pcm success "+wavtopcm)
        return pcmname

    #文件读取
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 调用baidu api接口转换为文字
    def to_baidu(self,pcmpath):
        result = self.client.asr(self.get_file_content(pcmpath), 'pcm', 16000, {'dev_pid': 1537,})
        text = ''
        if(result['err_no']==0):
            text = result['result'][-1]
            self.logger.info(str(self.chat_id)+" voiceTotext "+text)
        return text

    def run(self):
        ogapath = self.saveVoice(self.voice)
        wavpath = self.oga_to_wav(ogapath)
        pcmpath = self.wav_to_pcm(wavpath)
        text = self.to_baidu(pcmpath)
        return text


if __name__ == '__main__':
    pass
    # print(voiceTotext('1231231', "voice/1123223001-1586079280.oga").run())

