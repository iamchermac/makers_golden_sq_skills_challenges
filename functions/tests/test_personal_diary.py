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

def test_count_of_five_words():
    criteria = 5
    response = count_words("Here I go again, wow!")
    assert response ==  criteria

def test_count_of_a_tale_of_two_cities():
    criteria = 18
    response = count_words("It was the best of times, it was the worst of times, it was the age of wisdom.")
    assert response ==  criteria
    