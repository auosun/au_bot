import time
import qrcode
def getqrcode(content,chat_id):

    url = '{}{}-{}.png'.format('trash/qrcode/',chat_id,int(time.time()))
    q = qrcode.main.QRCode()
    q.add_data(content)
    q.make()
    img = q.make_image()
    img.save(url)
    return url
