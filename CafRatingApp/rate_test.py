# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# rate_test.py

import rate
import datetime


def test_positive() -> bool:
    # function body
    print("test_positive")
    dt = datetime.datetime.now()
    rate.update("123", dt, "meal1", "good")
    print("updated")

    record = rate.read("123", dt)
    print("record =" + record[0] + "," + record[1])

    return True
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
