# This is a sample Python script.
from typing import Any


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# rate.py

# rate.update function takes four parameter and stores/append to a file name cafRatingDB.txt
def update(id: Any,
           date: Any,
           meal: Any,
           rating: Any):
    # function body
    print("you are in rate.update function")
    print("parameters passed in are" + id + "," + date + "," + meal + "," + rating)

    return True

# rate.read function takes id and date. The fuction will read the DB and return the associated date associated
# with the ID and date.
def read(id: Any,
         date: Any) -> list[str]:
    # function body
    print("you are in rate.update function")
    print("parameters passed in are" + id + "," + date)
    record = ["id", "date", "meal", "rating"]
    return record


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
