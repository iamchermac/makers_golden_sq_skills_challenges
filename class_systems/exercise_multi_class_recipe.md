# {{PROBLEM}} Test-drive a Multi-Class Program Design Recipe

## 1. Describe the Problem

_As a user  
I would like to have a diary  
and be able to add entries to it_

_As a user  
I would like to determine how many minutes I would need  
to read all diary entries,  
based on how many words I can read in one minute_

_As a user  
I would like to read an entry from my diary  
based on the time I have available to read,  
and my reading speed_

## 2. Design the Interface for each Class

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass
```

```python

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
When we add an entry to the diary
We get the entry back in the list of diary entries
"""
diary = Diary()
entry = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
diary.add(entry)
diary.all() # => [entry]

"""
Given a reading speed of 10 words per minute
#reading_time returns an estimated time of 2 minutes, to read all diary entries
"""
diary = Diary()
entry_1 = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
entry_2 = DiaryEntry("Captain's Log, Stardate 2368.3", "It is hump day.")
entry_3 = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
entry_4 = DiaryEntry("Captain's Log, Stardate 2370.3", "TFIF, Hurrah!")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.add(entry_4)
diary.reading_time(10) # => 2

"""
Given a reading speed of 2 words per minute, with 1 available minute for reading
#find_best_entry_for_reading_time returns the fourth entry from the diary
"""
diary = Diary()
entry_1 = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
entry_2 = DiaryEntry("Captain's Log, Stardate 2368.3", "It is hump day.")
entry_3 = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
entry_4 = DiaryEntry("Captain's Log, Stardate 2370.3", "TFIF, Hurrah!")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.add(entry_4)
diary.reading_time(10) # => "TFIF, Hurrah!"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
