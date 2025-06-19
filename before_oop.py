# implement to do list
tasks = []

valid_statuses = {"pending", "in progress", "done"}

# task = {
#     "title": "Pickles",
#     "description": "Buy cucumbers and salt, and mustard seeds",
#     "status": "pending"
# }

def add_task(title, description, status):
    # create a new task
    for t in tasks:
        if t["title"] == title:
    #         we have a duplicate task, stop the function
            return
    # check for duplicate task title
    task = {
        "title": title,
        "description": description,
        "status": status
    }
    # add task to db
    tasks.append(task)


def update_status(title, new_status):
    if new_status in valid_statuses:
        for t in tasks:
            if t["title"] == title:
                t["status"] = new_status

        print("Update task")
    else:
        print("Statusul {} not valid ".format(new_status))

def print_tasks():
    for task in tasks:
        print(task)

add_task("Pickles", "Buy cucumbers and salt, and mustard seeds", "in_progress")
add_task("Dishes", "Wash the dishes", "in_progress")
add_task("Workout", "Go to the gym", "done")
add_task("Workout", "Looking ", "done")

update_status("Dishes", "not done")
update_status("Play", "done")
print_tasks()