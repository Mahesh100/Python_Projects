

from pyzbar.pyzbar import decode

from PIL import Image

decode(Image.open('D:/Python_Project/Project_06_QR_CODE/qrcode1.png'))
img = Image.open('D:/Python_Project/Project_06_QR_CODE/qrcode1.png')

result = decode(img)

print(result)