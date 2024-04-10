class TaskList:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        #   Creates a holder for tasks within the self object
        self.name = name
        self._tasks = []

    def add_todo(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the task holder of the self object
        self._tasks.append(task)

    def list_todo(self):
        # Returns:
        #   An indexed list of tasks the user needs to complete
        # Side-effects:
        #   Throws an exception if no task is set
        if not self._tasks:
            raise Exception("There are no tasks in the todo list.")
        else:
            return {index + 1: self._tasks[index] for index in range(0, len(self._tasks))}

    def mark_completed(self, task_index):
        # Parameters:
        #   task_index: integer
        # Returns:
        #   Nothing
        # Sid-effects
        #   Removes completed tasks from list of tasks
        self._tasks.pop(task_index - 1)
