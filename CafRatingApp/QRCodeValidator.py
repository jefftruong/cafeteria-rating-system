# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Python program to Scan and Read a QR code
# from qrtools import QR
#import QRCodeValidator
import cv2
#from cv2 import cv2
import numpy as np

# IRCodeValidator.py

# IRCodeValidator.read function controls the camera and read the qrcode. You should print out the QRCode.
def read():
    # function body
    img = cv2.imread(r"./static/Image/101520232252.png")
    detector = cv2.QRCodeDetector()
    val, b, c = detector.detectAndDecode(img)
    # my_QR = qrtools.QR()
    # my_QR.decode(filename="./static/Image/101520232252.png")

    # decodes the QR code and returns True if successful
    # my_QR.decode()

    # prints the data
    print(val)
    suc = False
    print("you are in IRCodeValidator.read")

    print("attempting to read qr code")
    suc = True

    return suc


if __name__ == '__main__':
    read()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
