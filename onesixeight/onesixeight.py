from sys import argv
import csv
import datetime

from app import ProjectItem, db

"""
Usage:

Add an entry:

$ onesixeight add

List all entries:

$ onesixeight list

Calculate critical path:

$ onesixeight crunch
"""


def add():
    title = input("Item title? ")
    start_date = input("Start date? ")
    hours_to_complete = input("Hours to complete? ")

    list_items()


    dependancy = input("Dependancy? ")

#    with open('./onesixeight.csv', 'r') as f:
#        reader = csv.reader(f)
#        for row in reader:
#            print(row)

    projectkwargs = {
        "title": title,
        "start_date": start_date or None,
        "hours_to_complete": hours_to_complete,
        "parent_id": dependancy
    }

    aproject = ProjectItem(**projectkwargs)

    db.session.add(aproject)
    db.session.commit()


def list_items():
    items = ProjectItem.query.all()
    for item in items:
        print("{}: {}, {}, {}".format(item.id, item.title, item.start_date, item.finish))


def update_item():
    list_items()
    item_id = input("ID of the item to update? ")

    element_to_update = input("Position to update? ")
    value = input("Updated value? ")

    with open('./onesixeight.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row_to_update)


START_DATE = datetime.date.today()
HOURS_PER_WORKDAY = 6
WORKDAYS_PER_WEEK = 6


def crunch():
    with open('./onesixeight.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [r for r in reader]
    total_hours = sum([int(i[2]) for i in rows])

    days_of_work = total_hours / HOURS_PER_WORKDAY
    weeks_of_work = days_of_work / WORKDAYS_PER_WEEK
    completion_date = START_DATE + datetime.timedelta(weeks=weeks_of_work)

    print("Days of work: {}".format(days_of_work))
    print("Completion date: {}".format(completion_date))


if __name__ == '__main__':
    command = argv[1]
    if command == 'add':
        add()
    elif command == 'list':
        list_items()
    elif command == 'update':
        update_item()
    elif command == 'crunch':
        crunch()
    else:
        print("Command not found.")
        exit(1)
