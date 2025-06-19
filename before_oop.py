# implement to do list
tasks = []

valid_statuses = {"pending", "in_progress", "done"}

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
            print("Duplicate tasks ! '{}'".format(title))
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

        # only show "Updated task!" if a task has actually beed updated, and not if we are given an invalid title
        has_been_updated = False

        for t in tasks:
            if t["title"] == title:
                t["status"] = new_status
                has_been_updated = True
        if has_been_updated:
            print("Updated task!")
        else:
            print("Task '{}' not found".format(title))
        print("Update task")
    else:
        print("Statusul '{}' not valid ".format(new_status))

def remove_task(title):
    # remove taks from our db
    for task in tasks:
        if task["title"] == title:
#             found task Now delete from db
            tasks.remove(task)
            print("Taks '{}' has beed deleted".format(title))


def list_tasks_by_status(status):
    # return all tasks that have the given status
    if status in valid_statuses:
        filtered_tasks = list(filter(lambda t: t["status"] == status, tasks))
        return filtered_tasks

    else:
        print("Statusul '{}' invalid!".format(status))
        return []
        # filtered_taks = []
        # for task in tasks:
        #     if task["status"] == status:
        #         filtered_taks.append(task)
def print_tasks():
    for task in tasks:
        print(task)

add_task("Pickles", "Buy cucumbers and salt, and mustard seeds", "in_progress")
add_task("Dishes", "Wash the dishes", "in_progress")
add_task("Workout", "Go to the gym", "done")
add_task("Workout", "Looking ", "done")
add_task("School", "Both ", "in_progress")
add_task("Life", "Get married ", "pending")
add_task("Workout", "Looking ", "done")

update_status("Dishes", "not done")
update_status("Play", "done")
remove_task("Dishes")
print(list_tasks_by_status("in_progress"))