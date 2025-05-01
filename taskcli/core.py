import json, datetime, os, argparse

file_path = "task_cli.json"


# Add task, initially marked as todo
def add(desc):
    date = datetime.datetime.now()
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    key = "tasks"
    if key not in data:
        data[key] = []
    elif not isinstance(data[key], list):
        raise ValueError(f"The key '{key}' exists but is not a list!")

    task = {
        "id": len(data[key]) + 1,  # simple auto-increment id
        "desc": desc,
        "created_at": date.strftime("%c"),
        "updated_at": None,
        "status": "todo",
    }

    data[key].append(task)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Task added successfully (ID:{task["id"]})")


# Update the description of the task
def update(id, updated_desc):
    with open(file_path, "r") as f:
        data = json.load(f)
    date = datetime.datetime.now()
    new_data = {
        "id": id,
        "desc": updated_desc,
        "created_at": data["tasks"][id - 1]["created_at"],
        "updated_at": date.strftime("%c"),
        "status": "todo",
    }

    data["tasks"][id - 1] = new_data
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Task updated successfully (ID:{id})")


# Change the status of the task - mark-done, mark-in-progress
def mark(id, status):
    with open(file_path, "r") as f:
        data = json.load(f)
        date = datetime.datetime.now()
        new_data = {
            "id": id,
            "desc": data["tasks"][id - 1]["desc"],
            "created_at": data["tasks"][id - 1]["created_at"],
            "updated_at": date.strftime("%c"),
            "status": status,
        }
    data["tasks"][id - 1] = new_data
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Task ID:{id} Marked as {status}")


# List tasks
def list_tasks(status):
    with open(file_path, "r") as f:
        data = json.load(f)
        data = data["tasks"]
        if status == None:
            for task in data:
                print(
                    f"""ID-{task["id"]}.   - Description: {task["desc"]}
          Created at: {task["created_at"]}
          Updated at: {task["updated_at"]}
          Status: {task["status"]}\n"""
                )
        else:
            for task in data:
                for k, v in task.items():
                    if k == "status" and v == status:
                        print(
                            f"""ID-{task["id"]}.   - Description: {task["desc"]}
                                - Created at: {task["created_at"]}
                                - Updated at: {task["updated_at"]}
                                - Status: {task["status"]}"""
                        )
