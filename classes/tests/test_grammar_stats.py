from lib.grammar_stats import *

"""
Given a valid sentence (a statement) that starts with a capitalized letter
A boolean of True is returned
"""
def test_capital_statement_returns_True():
    criteria = True
    gramstat = GrammarStats()
    response = gramstat.check("To be, or not to be, that is the question.")
    assert response == criteria

"""
Given a valid sentence (a question) that starts with a capitalized letter
A boolean of True is returned
"""
def test_capital_question_returns_True():
    criteria = True
    gramstat = GrammarStats()
    response = gramstat.check("To be, or not to be, that is the question?")
    assert response == criteria

"""
Given a valid sentence (statement of strong feeling) that starts with a capitalized letter
A boolean of True is returned
"""
def test_capital_exclamatory_returns_True():
    criteria = True
    gramstat = GrammarStats()
    response = gramstat.check("To be, or not to be, that is the question!")
    assert response == criteria

"""
Given a statement that does not start with a capitalized letter
A boolean of False is returned
"""
def test_uncapitalized_statement_returns_False():
    criteria = False
    gramstat = GrammarStats()
    response = gramstat.check("to be, or not to be, that is the question.")
    assert response == criteria

"""
Given a text snippet that starts with a capitalized letter but no sentence-ending punctuation
A boolean of False is returned
"""
def test_capital_with_no_sentence_ending_returns_False():
    criteria = False
    gramstat = GrammarStats()
    response = gramstat.check("To be, or not to be, that is the question")
    assert response == criteria

"""
A request for a percentage of text that have passed checks
Returns an integer representing percentage passed (e.g. 55 equals 55%)
"""
def test_percentage_good_returns_60():
    criteria = 60
    gramstat = GrammarStats()
    gramstat.check("To be, or not to be, that is the question.")
    gramstat.check("To be, or not to be, that is the question?")
    gramstat.check("To be, or not to be, that is the question!")
    gramstat.check("to be, or not to be, that is the question.")
    gramstat.check("To be, or not to be, that is the question")
    response = gramstat.percentage_good()
    assert response == criteria

def test_percentage_good_returns_100_100_100_75_60():
    criteria = [100,100,100,75,60]
    response = []
    gramstat = GrammarStats()
    gramstat.check("To be, or not to be, that is the question.")
    response.append(gramstat.percentage_good())
    gramstat.check("To be, or not to be, that is the question?")
    response.append(gramstat.percentage_good())
    gramstat.check("To be, or not to be, that is the question!")
    response.append(gramstat.percentage_good())
    gramstat.check("to be, or not to be, that is the question.")
    response.append(gramstat.percentage_good())
    gramstat.check("To be, or not to be, that is the question")
    response.append(gramstat.percentage_good())
    for i in range(0,len(criteria)):
        assert response[i] == criteria[i]
