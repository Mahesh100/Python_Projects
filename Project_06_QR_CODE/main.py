# pip install qrcode
# pip install pillow 

import qrcode

data = ' forget to Take Nap'

img = qrcode.make(data)

img.save('D:/Python_Project/Project_06_QR_CODE/qrcode.png')



