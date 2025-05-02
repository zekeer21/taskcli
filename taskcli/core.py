import json
import os
from datetime import datetime

FILE_PATH = "task_cli.json"
TASKS_KEY = "tasks"


def _load_data():
    """Safely load data from the JSON file."""
    if not os.path.exists(FILE_PATH):
        return {TASKS_KEY: []}
    with open(FILE_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {TASKS_KEY: []}  # fallback if file is empty or corrupt


def _save_data(data):
    """Save data to the JSON file."""
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def _generate_id(tasks):
    return 1 if not tasks else max(task["id"] for task in tasks) + 1


def add(description):
    data = _load_data()
    task_id = _generate_id(data[TASKS_KEY])
    task = {
        "id": task_id,
        "desc": description,
        "created_at": datetime.now().strftime("%x %X"),
        "updated_at": None,
        "status": "todo",
    }
    data[TASKS_KEY].append(task)
    _save_data(data)
    print(f"✅ Task added (ID: {task_id})")


def update(task_id, description):
    data = _load_data()
    for task in data[TASKS_KEY]:
        if task["id"] == task_id:
            task["desc"] = description
            task["updated_at"] = datetime.now().strftime("%x %X")
            _save_data(data)
            print(f"✏️ Task {task_id} updated.")
            return
    print(f"❌ Task {task_id} not found.")


def mark(task_id, status):
    data = _load_data()
    for task in data[TASKS_KEY]:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().strftime("%x %X")
            _save_data(data)
            print(f"🏷️ Task {task_id} marked as {status}.")
            return
    print(f"❌ Task {task_id} not found.")


def list_tasks(status=None):
    data = _load_data()
    tasks = data.get(TASKS_KEY, [])

    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if not tasks:
        print("📭 No tasks found.")
        return
    print(
        """ID     DESCRIPTION     STATUS            CREATED AT              UPDATED AT"""
    )
    for task in tasks:
        print(
            f"[{task['id']}] \t{task['desc']} \t({task['status']}) \t\t{task['created_at']} \t{task['updated_at']}"
        )


def delete(task_id):
    data = _load_data()
    for task in data[TASKS_KEY]:
        if task["id"] == task_id:
            data[TASKS_KEY].remove(task)
            _save_data(data)
            print(f"🗑️ Task {task_id} deleted.")
            return
    print(f"❌ Task {task_id} not found.")


def clear():
    """Clear all tasks."""
    data = _load_data()
    print("⚠️ Are you sure you want to clear all tasks? (y/n)")
    confirmation = input().strip().lower()
    if confirmation != "y":
        print("❌ Clear operation cancelled.")
        return
    # Proceed with clearing tasks
    data[TASKS_KEY] = []
    _save_data(data)
    print("🧹 All tasks cleared.")
