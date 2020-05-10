class auConfigs():
    def __init__(self):
        # Telegram bot api token
        self.token = ''

        # REQUEST_KWARGS
        self.proxy = {'proxy_url': '',}

        # Baidu voice api
        self.BAIDU_VOICE_API_ID = ''
        self.BAIDU_VOICE_API_KEY = ''
        self.BAIDU_VOICE_SECRET_KEY = ''

        # ffmpeg file address
        self.ffmpeg = ''

        # show proxy password
        self.proxy_password = ''

        # proxy data
        self.proxy_mtp = ''
        self.proxy_http = ''
        self.proxy_socks = ''
        self.proxy_v2ray = ''
        self.proxy_switch = ''

    def get_token(self):
        return self.token

    # 即将重构 删除get_proxy
    def get_proxy(self,args):
        text = '请仔细阅读 /proxy'
        if(len(args)==1 and args[0]=='mtp'):
            text = self.proxy_mtp

        if(len(args)==2):
            if(args[0] == self.proxy_password):
                if (args[1] == 'http'):
                    text = self.proxy_http
                elif (args[1] == 'socks'):
                    text = self.proxy_socks
                elif (args[1] == 'v2ray'):
                    text = self.proxy_v2ray
                elif (args[1] == 'switch'):
                    text = self.proxy_switch
                else:
                    text = '暂不提供'
            else:
                text = '密码错误'

        return text
