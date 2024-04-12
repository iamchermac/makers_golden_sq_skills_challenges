from lib.todo_list import *
from lib.todo import *

"""
When we add a todo to the todo list
We can access the todo in the list of incomplete todos
"""
def test_add_todo_to_incomplete():
    todo_list = TodoList()
    todo_entry_1 = Todo("Buy ingredients for Taco Tuesday.")
    todo_entry_2 = Todo("Buy a large skillet.")
    todo_entry_3 = Todo("Send out invites.")
    criteria = [todo_entry_1, todo_entry_2, todo_entry_3]
    todo_list.add(todo_entry_1)
    todo_list.add(todo_entry_2)
    todo_list.add(todo_entry_3)
    response = todo_list.incomplete()
    assert response == criteria

"""
When we call #give_up
All todos are placed in the list of complete todos
"""
def test_todo_list_give_up():
    todo_list = TodoList()
    todo_entry_1 = Todo("Buy ingredients for Taco Tuesday.")
    todo_entry_2 = Todo("Buy a large skillet.")
    todo_entry_3 = Todo("Send out invites.")
    criteria = [todo_entry_1, todo_entry_2, todo_entry_3]
    todo_list.add(todo_entry_1)
    todo_list.add(todo_entry_2)
    todo_list.add(todo_entry_3)
    todo_list.give_up()
    response = todo_list.complete()
    assert response == criteria
