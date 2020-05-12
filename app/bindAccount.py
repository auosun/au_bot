import mysql
import uuid
from v2ray_api import v2rayController
from config.config import auConfigs
def bindAccount(user_info,args):
    reply_text = '绑定失败'
    id = user_info['id']
    email = args
    first_name = user_info['first_name']
    last_name = user_info['last_name']
    myuuid = uuid.uuid4().hex
    sql = "INSERT INTO `user` " \
          "(`id`, `email`, `first_name`,`last_name`,`register_time`, `uuid`)" \
          "VALUES ('%d', '%s', '%s', '%s', now(),'%s');"%\
          (id,email,first_name,last_name,myuuid)
    result = mysql.mysql(sql)
    status = v2rayController.create_user_in_v2ray_server(auConfigs().ip,email)
    if(result):
        if(status == 1):
            reply_text = '绑定成功, '
        else:
            reply_text = '绑定成功，但创建v2ray用户失败，请联系管理员'

    return reply_text