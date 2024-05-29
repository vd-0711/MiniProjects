# !pip install segno
import segno
from urllib.request import urlopen
qrcode = segno.make('https://www.youtube.com/watch?v=nUcm_hokUIc', error='h')
#segno.make_qr() // creates normal qr code for any link/text
url = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzZyZmMwd290dGoyd2V0bWF1b2Fkb3A3NGU3cHhzcHB0MjFxaHNoZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2R0cE5EqO3QHiCoU/giphy.gif"
url_open = urlopen(url)
#qr.save("basic_qrcode.png" , scale =10 , border= 0, light = 'darkblue', dark = 'white') // to save normal qr
qrcode.to_artistic( background=url_open,target='Generated.gif', scale=10 ) #to generate qr with image/gif backgrounds
print("QR generated successfully")
