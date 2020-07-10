import pytest

TODO_TXT_LOCATION = "../tests/todo.txt"

todofile_contents """
    (D) this is the first task start:2020-06-12 duration:3d critical:y 168id:1\n
    (A) this is the second task duration:1w critical:y 168id:2 parent:1\n
    (C) this is the third task start:2020-06-08 duration:5h critical:y 168id:3 parent:2\n
    (A) this is the fourth task start:2020-07-14 duration:5h critical:n 168id:4 parent:3\n
"""

RE_SEARCH = r"start:[-\d]{10}"
RE_DURATION = r"duration:[\w]{1,3}"


def test_fetch_todotxt_tasks():
    """If I call onesixeight_todotxt.py#get_todotxt_tasks(), it should return a
    dictionary of tasks."""

    for task in todofile_contents.split("\n"):
        task_dict = dict(
            duration=re.search(RE_SEARCH, task)[0],
            duration=re.search(RE_DURA0`


    tasks = {
        dict(title="Do the first thing",

    }
