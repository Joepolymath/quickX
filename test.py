import qrcode
import os
msg = input("Type in your message here:  ")
qr = qrcode.make(msg)
name = input("File Name:  ")
file_name = name + '.png'
qr.save(file_name)
