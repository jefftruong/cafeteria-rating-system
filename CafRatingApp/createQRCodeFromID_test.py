# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# createQRCodeFromID_test.py

# tests for createQRCodeFromID.py
import createQRCodeFromID


def test_positive() -> bool:
    # function body
    suc = createQRCodeFromID.create("101520231739")

    if suc:
        print("was able to read qr code successfully")
    else:
        print("was able to read qr code unsuccessfully")

    return True
