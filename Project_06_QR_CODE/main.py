# pip install qrcode
# pip install pillow 
# pip install pyzbar (to decode QRcode)

import qrcode

data = ' forget to Take Nap'
qr = qrcode.QRCode(version= 1, box_size =10, border= 5 )

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color ='red', back_color ='white')

img.save('D:/Python_Project/Project_06_QR_CODE/qrcode1.png')

img = qr.make_image(fill_color = 'green', back_color = 'yellow')

img.save('D:/Python_Project/Project_06_QR_CODE/qrcode2.png')



img = qrcode.make(data)

img.save('D:/Python_Project/Project_06_QR_CODE/qrcode.png')

print('Check your source folder')



