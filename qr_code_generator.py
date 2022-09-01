import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "www.google.com"
  
# Generate QR code 
QR = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
QR.svg("google.svg", scale = 8)