import argparse
from taskcli.core import add, update, mark, list_tasks


def handle_add(args):
    add(args.description)


def handle_update(args):
    update(args.id, args.description)


def handle_mark_in_progress(args):
    mark(args.id, "in-progress")


def handle_mark_done(args):
    mark(args.id, "done")


def handle_list(args):
    list_tasks(args.status)


def main():
    parser = argparse.ArgumentParser(
        description="Task CLI: add, update, mark, and list your tasks."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")
    add_parser.set_defaults(func=handle_add)

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task description")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("description", type=str, help="New description")
    update_parser.set_defaults(func=handle_update)

    # Mark in-progress command
    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Mark a task as in-progress"
    )
    mark_in_progress_parser.add_argument("id", type=int, help="ID of the task to mark")
    mark_in_progress_parser.set_defaults(func=handle_mark_in_progress)

    # Mark done command
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=int, help="ID of the task to mark")
    mark_done_parser.set_defaults(func=handle_mark_done)

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "status",
        type=str,
        nargs="?",
        choices=["done", "todo", "in-progress"],
        help="Optional: filter tasks by status",
    )
    list_parser.set_defaults(func=handle_list)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
