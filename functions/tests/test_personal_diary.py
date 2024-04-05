from lib.personal_diary import *

def test_snippet_of_sentence_with_seven_words():
    criteria = "Here I go again on..."
    response = make_snippet("Here I go again on my own!")
    assert response ==  criteria

def test_snippet_of_sentence_with_four_words():
    criteria = "Here I go again!"
    response = make_snippet("Here I go again!")
    assert response ==  criteria

def test_snippet_of_sentence_with_five_words():
    criteria = "Here I go again, wow!"
    response = make_snippet("Here I go again, wow!")
    assert response ==  criteria
    