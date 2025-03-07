#TODO

1. Install Python: Python is usually installed by default on most modern systems. To check what your currently have, open a terminal and run the following command

	```
	  python3 --version

	```
  This should output some information on the installed Python version.
	You can also install ruby by following these instructions. https://installpython3.com/

2. You are expected to write the code in `todo.py` file.


## Specification

1. The app can be run in the console with `todo.bat`.

2. The app should read from and write to a `todo.txt` text file. Each todo item occupies a single line in this file. Here is an example file that has 2 todo items.

```txt
water the plants
change light bulb
```

3.  When a todo item is completed, it should be removed from `todo.txt` and instead added to the `done.txt` text file. This file has a different format:

    ```txt
    x 2020-06-12 the text contents of the todo item
    ```

    1. the letter x
    2. the current date in `yyyy-mm-dd` format
    3. the original text

    The date when the todo is marked as completed is recorded in the `yyyy-mm-dd` format (ISO 8601). For example, a date like `15th August, 2020` is represented as `2020-08-15`.

4.  The application must open the files `todo.txt` and `done.txt` from where the app is run, and not where the app is located. For example, if we invoke the app like this:

    ```
    $ cd ~/plans
    $ ~/apps/todo ls
    ```

    The application should look for the text files in `~/plans`, since that is the user’s current directory.

## Usage

### 1. Help

Executing the command without any arguments, or with a single argument `help` prints the CLI usage.

```
$ todo.bat todo help
Usage :-
  usage: todo.py todo [-h] [-add [ADD]] [-ls] [-del DEL] [-done DONE] [-report]

  optional arguments:
    -h, --help  show this help message and exit
    -add [ADD]  # Add a new todo
    -ls         # Show remaining todos
    -del DEL    # Delete a todo
    -done DONE  # Complete a todo
    -report     # Statistics
```

### 2. List all pending todos

Use the `ls` command to see all the todos that are not yet complete. The most recently added todo should be displayed first.

```
$ todo.bat todo ls
[2] change light bulb
[1] water the plants
```

### 3. Add a new todo

Use the `add` command. The text of the todo item should be enclosed within double quotes (otherwise only the first word is considered as the todo text, and the remaining words are treated as different arguments).

```
$ todo.bat todo add "the thing i need to do"
Added todo: "the thing i need to do"
```

### 4. Delete a todo item

Use the `del` command to remove a todo item by its number.

```
$ todo.bat todo del 3
Deleted todo #3
```

Attempting to delete a non-existent todo item should display an error message.

```
$ todo.bat todo del 5
Error: todo #5 does not exist. Nothing deleted.
```

### 5. Mark a todo item as completed

Use the `done` command to mark a todo item as completed by its number.

```
$ todo.bat todo done 1
Marked todo #1 as done.
```

Attempting to mark a non-existed todo item as completed will display an error message.

```
$ todo.bat todo done 5
Error: todo #5 does not exist.
```

### 6. Generate a report

Use the `report` command to see the latest tally of pending and completed todos.

```
$ todo.bat todo report
dd/mm/yyyy Pending : 1 Completed : 4
```
