# {{PROBLEM}} Function Design Recipe - Exercise One

## 1. Describe the Problem

_As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimated_reading_time(text, reading_rate_wpm):
    """Analyse some text and determine time taken to read it
        based on a reading rate

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "Four score and seven years ago our fathers brought forth...")
        reading_rate_wpm: (optional) a number (int or float) indicating how many words cna be read per minute

    Returns: (state the return value and its type)
        a string representing an error message or a time value, in minutes and seconds (e.g. 2 minutes, 15 seconds)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a snippet from the Gettysburg Address, with no optional reading rate
It returns a string denoting 0 minutes and 3 seconds
"""
estimated_reading_time("Four score and seven years ago our fathers brought forth") => "0 minutes, 3 seconds"

"""
Given a snippet from the Gettysburg Address and a reading rate of 20 words per minute
It returns a string denoting 0 minutes and 30 seconds
"""
estimated_reading_time("Four score and seven years ago our fathers brought forth", 20) => "0 minutes, 30 seconds"

"""
Given a snippet from the Gettysburg Address and a reading rate of 5 words per minute
It returns a string denoting 2 minutes and 0 seconds
"""
estimated_reading_time("Four score and seven years ago our fathers brought forth", 5) => "2 minutes, 0 seconds"

"""
Given an empty string
It returns an error message "You must provide a snippet with at least one word."
"""
estimated_reading_time("") => "You must provide a snippet with at least one word."

"""
Given a None value
It throws an error
"""
estimated_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

from lib.reading_time import *

"""
Given a snippet from the Gettysburg Address, with no optional reading rate
It returns a string denoting 0 minutes and 3 seconds
"""
def test_gettys_address_returns_0_mins_3_secs():
    criteria = "0 minutes, 3 seconds"
    response = estimated_reading_time("Four score and seven years ago our fathers brought forth")
    assert response == criteria

"""
Given a snippet from the Gettysburg Address and a reading rate of 20 words per minute
It returns a string denoting 0 minutes and 30 seconds
"""
def test_gettys_address_20wpm_returns_0_mins_30_secs():
    criteria = "0 minutes, 30 seconds"
    response = estimated_reading_time("Four score and seven years ago our fathers brought forth", 20)
    assert response == criteria

"""
Given a snippet from the Gettysburg Address and a reading rate of 5 words per minute
It returns a string denoting 2 minutes and 0 seconds
"""
def test_gettys_address_5wpm_returns_2_mins_0_secs():
    criteria = "2 minutes, 0 seconds"
    response = estimated_reading_time("Four score and seven years ago our fathers brought forth", 5)
    assert response == criteria

"""
Given an empty string
It returns an error message "You must provide a snippet with at least one word."
"""
def test_empty_string_returns_special_error_message():
    criteria = "You must provide a snippet with at least one word."
    response = estimated_reading_time("")
    assert response == criteria

"""
Given a None value
It throws an error
"""
def test_none_returns_error_thrown():
    criteria = "A None object was given instead of some text."
    response = estimated_reading_time(None)
    assert response == criteria
```

Ensure all test function names are unique, otherwise pytest will ignore them!
