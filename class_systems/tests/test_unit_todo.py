from lib.todo import *

def test_todo_incomplete():
    task = "Buy ingredients for Taco Tuesday."
    todo = Todo(task)
    assert todo.task == task
    assert todo.complete == False

def test_todo_mark_complete():
    task = "Buy ingredients for Taco Tuesday."
    todo = Todo(task)
    todo.mark_complete()
    assert todo.task == task
    assert todo.complete == True
