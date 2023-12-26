# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Python program to Scan and Read a QR code
# from qrtools import QR
# import QRCodeValidator
import cv2
# from cv2 import cv2
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


def readcamera():
    # program to capture single image from webcam in python

    # importing OpenCV library
    import cv2

    # initialize the camera
    # If you have multiple camera connected with
    # current device, assign a value in cam_port
    # variable according to that
    cam_port = 0
    cam = VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

        # showing result, it take frame name and image
        # output
        imshow("GeeksForGeeks", image)

        # saving image in local storage
        imwrite("GeeksForGeeks.png", image)

        # If keyboard interrupt occurs, destroy image
        # window
        waitKey(0)
        destroyWindow("GeeksForGeeks")

        # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

    return


if __name__ == '__main__':
    readcamera()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
