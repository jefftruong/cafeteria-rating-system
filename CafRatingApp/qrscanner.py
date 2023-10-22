# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Python program to Scan and Read a QR code
import cv2
from colorama import init
from termcolor import colored
import webbrowser

# turn on camera and take picture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the webcam is opened correctly
print("checking webcam")

if not cap.isOpened():
    raise print("Cannot open webcam")
else:
    print("opened webcam")

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    success, img = cap.read()
    print("read is " + success.__str__())
    print(img.__str__())

    cv2.imwrite("./static/Image/scannedQRCode.png",img)

    detector = cv2.QRCodeDetector()
    val, b, c = detector.detectAndDecode(img)

    # check if there is a QRCode in the image
    if val:
        print("b = " + b.__str__())
        print("c =" + c.__str__())
        print(colored("ID = " + val.__str__(), 'green', 'on_yellow'))
        cv2.imshow("QRCODEScanner", img)
        # break
        # b = webbrowser.open(str(val))
        cap.release()
        cv2.destroyAllWindows()
        break

    time.sleep(3)


