class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, todo):
        self._todos.append(todo)

    def incomplete(self):
        return [todo for todo in self._todos if not todo.complete]

    def complete(self):
        return [todo for todo in self._todos if todo.complete]

    def give_up(self):
        for todo in self._todos:
            todo.mark_complete()
