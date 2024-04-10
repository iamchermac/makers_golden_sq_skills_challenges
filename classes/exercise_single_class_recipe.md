# {{PROBLEM}} Design a Single-Class Program - Design Recipe

## 1. Describe the Problem

_As a user  
So that I can keep track of my tasks  
I want a program that I can add todo tasks to and see a list of them._  

_As a user  
So that I can focus on tasks to complete  
I want to mark tasks as complete and have them disappear from the list._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskList:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        #   Creates a holder for tasks within the self object
        pass # No code here yet

    def add_todo(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the task holder of the self object
        pass # No code here yet

    def list_todo(self):
        # Returns:
        #   An indexed list of tasks the user needs to complete
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def mark_completed(self, task_index):
        # Parameters:
        #   task_index: integer
        # Returns:
        #   Nothing
        # Sid-effects
        #   Removes completed tasks from list of tasks
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a name and a task
#add_todo adds the task to the list of tasks to be completed
"""
tasks = TaskList("Paint the house")
tasks.add_todo("Buy some paint")

"""
Given a name and several tasks
#list_todo shows and indexed list of tasks to be completed
"""
tasks = TaskList("Paint the house")
tasks.add_todo("Buy some paint")
tasks.add_todo("Buy some rollers")
tasks.add_todo("Buy a roller pan")
tasks.add_todo("Mix paint")
tasks.add_todo("Pour paint into pan")
tasks.list_todo()  =>   {1: 'Buy some paint', 2: 'Buy some rollers', 3: 'Buy a roller pan', 4: 'Mix paint', 5: 'Pour paint into pan'}

"""
Given a name and no task
#list_todo raises an exception
"""
tasks = TaskList("Paint the house")
tasks.list_todo() # raises an error with the message "No task set."

"""
Given an index of a task
#mark_completed removes the associated task from list of tasks to be completed
"""
tasks = TaskList("Paint the house")
tasks.add_todo("Buy some paint")
tasks.add_todo("Buy some rollers")
tasks.add_todo("Buy a roller pan")
tasks.add_todo("Mix paint")
tasks.add_todo("Pour paint into pan")
tasks.mark_completed(3)
tasks.list_todo()  =>   {1: 'Buy some paint', 2: 'Buy some rollers', 3: 'Mix paint', 4: 'Pour paint into pan'}
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
```python

import pytest
from lib.task_list import TaskList

"""
Given a name and a task
#add_todo adds the task to the list of tasks to be completed
"""
def test_add_to():
    criteria1 = "Paint the house"
    criteria2 = ["Buy some paint"]
    tasks = TaskList("Paint the house")
    tasks.add_todo("Buy some paint")
    assert tasks.name == criteria1
    assert tasks._tasks == criteria2

"""
Given a name and several tasks
#list_todo shows and indexed list of tasks to be completed
"""
def test_list_todo():
    criteria = {1: 'Buy some paint', 2: 'Buy some rollers', 3: 'Buy a roller pan', 4: 'Mix paint', 5: 'Pour paint into pan'}
    tasks = TaskList("Paint the house")
    tasks.add_todo("Buy some paint")
    tasks.add_todo("Buy some rollers")
    tasks.add_todo("Buy a roller pan")
    tasks.add_todo("Mix paint")
    tasks.add_todo("Pour paint into pan")
    response = tasks.list_todo()
    assert response == criteria

"""
Given a name and no task
#list_todo raises an exception
"""
def test_list_todo_with_no_tasks():
    criteria = "There are no tasks in the todo list."
    tasks = TaskList("Paint the house")
    with pytest.raises(Exception) as err:
        tasks.list_todo()
    response = str(err.value)
    assert response == criteria

"""
Given an index of a task
#mark_completed removes the associated task from list of tasks to be completed
"""
def test_mark_completed():
    criteria = {1: 'Buy some paint', 2: 'Buy some rollers', 3: 'Mix paint', 4: 'Pour paint into pan'}
    tasks = TaskList("Paint the house")
    tasks.add_todo("Buy some paint")
    tasks.add_todo("Buy some rollers")
    tasks.add_todo("Buy a roller pan")
    tasks.add_todo("Mix paint")
    tasks.add_todo("Pour paint into pan")
    tasks.mark_completed(3)
    response = tasks.list_todo()
    assert response == criteria
```

Ensure all test function names are unique, otherwise pytest will ignore them!
