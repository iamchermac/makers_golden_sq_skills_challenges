from lib.todo_list import *

def test_todo_list_incomplete_no_tasks_added_returns_empty_list():
    criteria = []
    todo_list = TodoList()
    response = todo_list.incomplete()
    assert response == criteria

def test_todo_list_complete_no_tasks_added_returns_empty_list():
    criteria = []
    todo_list = TodoList()
    response = todo_list.complete()
    assert response == criteria
