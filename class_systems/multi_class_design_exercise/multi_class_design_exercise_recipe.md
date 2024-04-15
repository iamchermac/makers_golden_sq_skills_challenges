# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_As a user  
So that I can record my experiences  
I want to keep a regular diary_ 

_As a user  
So that I can reflect on my experiences  
I want to read my past diary entries_

_As a user  
So that I can reflect on my experiences in my busy day  
I want to select diary entries to read based on how much time I have and my reading speed_

_As a user  
So that I can keep track of my tasks  
I want to keep a todo list along with my diary_

_As a user  
So that I can keep track of my contacts  
I want to see a list of all of the mobile phone numbers in all my diary entries_

## 2. Design the Class System

_Also design the interface of each class in more detail._

```python
class Diary:
    def __init__(self):
        # Side-effects:
        #   Creates a list for diary entries
        #   Creates a todo_list object as an instance of TodoList
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry or TodoEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the diary entries list or todo_list depending on type
        pass

    def show_all_diary_entries():
        # Returns:
        #   a formatted string representing all diary entries
        pass

class TodoList:
    def __init__(self):
        # Side-effects:
        #   Creates a list for todo entries
        pass # No code here yet

    def add(self, todo):
        # Parameters:
        #   todo: an instance of TodoEntry
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the todo to the todo holder of the self object
        pass # No code here yet


class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass
    
    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

class TodoEntry:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
Given a diary
When we add a diary entry
We see those entries reflected in the list of diary entries
"""
diary = Diary()
entry = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
diary.add(entry)
diary._entries # => [entry]

"""
Given a diary
When we add a todo entry
The todo entry is reflected in the list of todo entries in the TodoList instance
"""
diary = Diary()
entry = TodoEntry("Buy some milk.")
diary._todo_list.add(entry)
diary._todo_list._entries # => [entry]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
