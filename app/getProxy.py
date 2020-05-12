from config.config import auConfigs

def getProxy(args):

    proxy_password = auConfigs().proxy_password

    proxy_public_mtp = '暂不提供'

    proxy_http = '暂不提供'
    proxy_socks = '暂不提供'
    proxy_v2ray = '暂不提供'
    proxy_switch = '暂不提供'
    proxy_ss = '暂不提供'
    proxy_mtp = '暂不提供'

    text = '请仔细阅读 /proxy'
    if (len(args) == 1 and args[0] == 'mtp'):
        text = proxy_public_mtp

    if (len(args) == 2):
        if (args[0] == proxy_password):
            if (args[1] == 'http'):
                text = proxy_http
            elif (args[1] == 'socks'):
                text = proxy_socks
            elif (args[1] == 'v2ray'):
                text = proxy_v2ray
            elif (args[1] == 'switch'):
                text = proxy_switch
            elif (args[1] == 'ss'):
                text = proxy_ss
            elif (args[1] == 'mtp'):
                text = proxy_mtp
            else:
                text = '暂不提供'
        else:
            text = '密码错误'

    return text