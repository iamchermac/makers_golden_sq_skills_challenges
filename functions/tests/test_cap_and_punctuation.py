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
