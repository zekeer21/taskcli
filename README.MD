# TaskCLI

TaskCLI is a simple command-line application designed to help you manage your tasks efficiently. With TaskCLI, you can add, view, and organize your tasks directly from the terminal.

## Installation

Follow these steps to install TaskCLI:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/zekeer21/taskcli.git
   cd taskcli
   ```

2. **Set Up a Virtual Environment (Optional)**
   If you want to use a virtual environment, you can set it up with the following commands:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python taskcli.py
   ```

Alternatively, you can skip this step if you prefer to install the application globally.

5. **Install Globally Using pipx (Optional)**

If you want to install TaskCLI globally and isolate it from other Python packages, you can use `pipx`:

```bash
pip install pipx
pipx install .
```

This will allow you to run `taskcli` from anywhere in your terminal.

6. **Uninstalling TaskCLI**

If you installed TaskCLI using `pipx`, you can uninstall it with:

```bash
pipx uninstall taskcli
```

If you installed it in a virtual environment, simply deactivate the environment and delete the folder.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Now you're ready to start managing your tasks with TaskCLI!

## Usage

Once TaskCLI is installed, you can use the following commands to manage your tasks:

### Adding a Task

To add a new task, use the `add` command followed by the task description:

```bash
taskcli add "Buy groceries"
```

### Viewing Tasks

To view all your tasks, use the `list` command:

```bash
taskcli list
```

### Marking a Task as Complete

To mark a task as done, use the `mark-done` command followed by the task ID:

```bash
taskcli mark-done 1
```

### Deleting a Task

To delete a task, use the `delete` command followed by the task ID:

```bash
taskcli delete 1
```

### Clearing All Tasks

To remove all tasks, use the `clear` command:

```bash
taskcli clear
```

### Viewing Help

To see a list of all available commands and their usage, use the `help` command:

```bash
taskcli --help
```

Now you can efficiently manage your tasks using TaskCLI!
