# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# QRCodeValidator_test.py

# tests for QRCodeValidator.py
import QRCodeValidator


def test_positive() -> bool:
    # function body
    suc = QRCodeValidator.read()
    if suc:
        print("was able to read qr code successfully")
    else:
        print("was not able to read qr code")

    return True
