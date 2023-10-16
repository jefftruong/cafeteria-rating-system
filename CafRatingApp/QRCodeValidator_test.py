import QRCodeValidator


def test_positive() -> bool:
    # function body
    suc = QRCodeValidator.read()
    if suc:
        print("was able to read qr code successfully")
    else:
        print("was able to read qr code unsuccessfully")

    return True
