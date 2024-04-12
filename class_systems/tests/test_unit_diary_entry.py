from lib.diary_entry import *

def test_diary_entry():
    title = "Captain's Log, Stardate 2367.3"
    contents = "It is Taco Tuesday."
    entry = DiaryEntry(title, contents)
    assert entry.title == title
    assert entry.contents == contents

def test_diary_entry_count_words_returns_4():
    criteria = 4
    title = "Captain's Log, Stardate 2367.3"
    contents = "It is Taco Tuesday."
    entry = DiaryEntry(title, contents)
    response = entry.count_words()
    assert response == criteria

def test_reading_time_5wpm_returns_2():
    criteria = 2
    entry = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    response = entry.reading_time(5)
    assert response == criteria

def test_reading_time_3wpm_returns_4():
    criteria = 4
    entry = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    response = entry.reading_time(3)
    assert response == criteria

def test_reading_chunk_twice_2wpm_2mins():
    criteria_1 = "Tonight is bin collection."
    criteria_2 = "I need to put"
    entry = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    assert entry.reading_chunk(2, 2) == criteria_1
    assert entry.reading_chunk(2, 2) == criteria_2

def test_reading_chunk_three_times_4wpm_1mins():
    criteria_1 = "Tonight is bin collection."
    criteria_2 = "I need to put"
    criteria_3 = "them out."
    entry = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    assert entry.reading_chunk(4, 1) == criteria_1
    assert entry.reading_chunk(4, 1) == criteria_2
    assert entry.reading_chunk(4, 1) == criteria_3
