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

        # admin account
        self.admin_chat_id = ''

    def get_token(self):
        return self.token

