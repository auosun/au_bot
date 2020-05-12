from v2ray_api.client import Client
import uuid
import mysql
import json
import base64
from config.config import auConfigs

def create_user_in_v2ray_server(ip,email):
    sql = "SELECT * FROM `user` WHERE `email` = '%s'"%(email)
    result = mysql.mysql(sql)
    if(result==1 or result==False):
        return 0
    try:
        c = Client(ip, 10085)
        c.add_user('vmess-in', result[0][5], email, 0, 2)
    except Exception:
        return 0

    return 1

def delete_user_in_v2ray_server(ip,email):
    try:
        c = Client(ip, 10085)
        c.remove_user('vmess-in', email)
    except Exception:
        return 0

    return 1

def get_vmess(id):
    sql = "SELECT * FROM `user` WHERE `id` = '%s'" % (id)
    result = mysql.mysql(sql)
    if (result == 1 or result == False):
        return 0
    myuuid = result[0][5]
    # print(myuuid)
    vmess = {"port":"443",
            "ps": auConfigs().v2_address,
            "tls":"tls",
            "id":str(uuid.UUID(myuuid)),
            "aid":"2",
            "v":"2",
            "host":auConfigs().v2_address,
            "type":"none",
            "path":"/f396791b/",
            "net":"ws",
            "add":auConfigs().v2_address}
    url = json.dumps(vmess)
    str_url = base64.b64encode(url.encode("utf-8"))
    return "vmess://"+str_url.decode('utf-8')



# if __name__ == '__main__':
    # ip =
    # email =
    # status = create_user_in_v2ray_server(ip, email)
    # print(status)
    # status = delete_user_in_v2ray_server(ip, email)
    # print(status)