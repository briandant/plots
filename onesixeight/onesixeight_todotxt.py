from todotxt import BaseToken, BaseDateToken, Task

import settings


# class TaskStartDate(BaseDateToken):
#     pass


# class DurationToken(BaseToken):
#     pass


# class OneSixEightTask(Task):
#     pass


def get_all_items():
    """Return a list of all the Task objects in todo.txt."""

    with open(settings.TODO_FILE, 'r') as f:
        for count, line in enumerate(f):
            print("Item {}: {}".format(count, line))


if __name__ == '__main__':
    get_all_items()
