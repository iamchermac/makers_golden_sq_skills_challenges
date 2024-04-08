# {{PROBLEM}} Function Design Recipe - Exercise One

## 1. Describe the Problem

_As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def capital_punctuation(text):
    """Analyse some text and determine if it starts with a capital letter and
        ends with appropriate sentence-ending punctuation

    Parameters: (list all parameters and their types)
        text: a string (e.g. "To be, or not to be, that is the question.")

    Returns: (state the return value and its type)
        a string indicating if the text is satisfactory or not.

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a statement that starts with a capitalized letter
It returns a string indicating a satisfactory sentence
"""
capital_punctuation("To be, or not to be, that is the question.") => "This text does have required capitals and does have required punctuation."

"""
Given a question that starts with a capitalized letter
It returns a string indicating a satisfactory sentence
"""
capital_punctuation("To be, or not to be, that is the question?") => "This text does have required capitals and does have required punctuation."

"""
Given a statement of strong feeling, that starts with a capitalized letter
It returns a string indicating a satisfactory sentence
"""
capital_punctuation("To be, or not to be, that is the question!") => "This text does have required capitals and does have required punctuation."

"""
Given a statement that does not start with a capitalized letter
It returns a string indicating an unsatisfactory sentence
"""
capital_punctuation("to be, or not to be, that is the question.") => "This text does not have required capitals but does have required punctuation."

"""
Given text that starts with a capitalized letter but no sentence-ending punctuation
It returns a string indicating an unsatisfactory sentence
"""
capital_punctuation("To be, or not to be, that is the question") => "This text does have required capitals but does not have required punctuation."

"""
Given an empty string
It returns an error message "You must provide text with at least one word."
"""
capital_punctuation("") => "You must provide text with at least one word."

"""
Given a None value
It throws an error
"""
capital_punctuation(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

import pytest
from lib.cap_and_punctuation import *

"""
Given a statement that starts with a capitalized letter
It returns a string indicating a satisfactory sentence
"""
def test_capital_statement_returns_satisfactory_indicator():
    criteria = "This text does have required capitals and does have required punctuation."
    response = capital_punctuation("To be, or not to be, that is the question.")
    assert response == criteria

"""
Given a question that starts with a capitalized letter
It returns a string indicating a satisfactory sentence
"""
def test_capital_question_returns_satisfactory_indicator():
    criteria = "This text does have required capitals and does have required punctuation."
    response = capital_punctuation("To be, or not to be, that is the question?")
    assert response == criteria

"""
Given a statement of strong feeling, that starts with a capitalized letter
It returns a string indicating a satisfactory sentence
"""
def test_capital_exclamatory_returns_satisfactory_indicator():
    criteria = "This text does have required capitals and does have required punctuation."
    response = capital_punctuation("To be, or not to be, that is the question!")
    assert response == criteria

"""
Given a statement that does not start with a capitalized letter
It returns a string indicating an unsatisfactory sentence
"""
def test_uncapitalized_statement_returns_unsatisfactory_indicator():
    criteria = "This text does not have required capitals but does have required punctuation."
    response = capital_punctuation("to be, or not to be, that is the question.")
    assert response == criteria

"""
Given text that starts with a capitalized letter but no sentence-ending punctuation
It returns a string indicating an unsatisfactory sentence
"""
def test_capital_with_no_sentence_ending_returns_unsatisfactory_indicator():
    criteria = "This text does have required capitals but does not have required punctuation."
    response = capital_punctuation("To be, or not to be, that is the question")
    assert response == criteria

"""
Given an empty string
It returns an error message "You must provide text with at least one word."
"""
def test_empty_string_returns_special_error_message():
    criteria = "You must provide text with at least one word."
    response = capital_punctuation("")
    assert response == criteria

"""
Given a None value
It throws an error
"""
def test_none_returns_error_thrown():
    criteria = "A None object was given instead of some text."
    with pytest.raises(Exception) as err:
        capital_punctuation(None)
    response = str(err.value)
    assert response == criteria
```

Ensure all test function names are unique, otherwise pytest will ignore them!
