import pyqrcode
import png
from pyqrcode import QRCode

QRString = 'https://www.instagram.com/renan.makoto/'

url = pyqrcode.create(QRString)

url.png(r'qr.png', scale=8)
