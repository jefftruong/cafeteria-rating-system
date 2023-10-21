from typing import Any

import tempfile


def update(id: any,
           date: any,
           meal: any,
           rating: any):
    # function body
    print("you are in rate.update function")
    print("parameters passed in are " + id + "," + date + "," + meal + "," + rating)
    'update.txt'
    file_path = 'update.txt'
    with open(file_path, 'a') as file:
        file.write(f'{id},{date},{meal},{rating}')

    return True


# rate.read function takes id and date. The function will read the DB and return the associated date associated
# with the ID and date.


def read(id: any,
         date: any) -> list[str]:
    # function body
    print("you are in rate.update function")
    print("parameters passed in are" + id + "," + date)
    record = ["id", "date", "meal", "rating"]
    return record


if not __name__ != '__main__':
    update("1234", "10182023", "apple", "good")