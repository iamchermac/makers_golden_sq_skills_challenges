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
