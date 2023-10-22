from typing import Any


def update(id: Any, date: Any, meal: Any, rating: Any) -> bool:
    print("you are in rate.update function")
    print("parameters passed in are " + id + "," + date + "," + meal + "," + rating)
    file_path = 'update.txt'
    with open(file_path, 'a') as file:
        file.write(f'{id},{date},{meal},{rating}\n')  # Append the values to the file with a newline character
    return True


def read(id: Any, date: Any) -> list[str]:
    print("you are in rate.read function")
    print("parameters passed in are " + id + "," + date)
    record = ["id", "date", "meal", "rating"]
    return record


if __name__ == '__main__':
    update("1234", "10182023", "apple", "good")
