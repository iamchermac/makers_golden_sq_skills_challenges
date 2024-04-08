import pytest
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
    with pytest.raises(Exception) as err:
        estimated_reading_time(None)
    response = str(err.value)
    assert response == criteria
    