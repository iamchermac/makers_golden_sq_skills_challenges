from lib.diary import *
from lib.diary_entry import *

"""
When we add an entry to the diary
We get the entry back in the list of diary entries
"""
def test_list_diary_entries():
    diary = Diary()
    entry = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
    criteria = [entry]
    diary.add(entry)
    response = diary.all()
    assert response == criteria

"""
Given a reading speed of 10 words per minute
#reading_time returns an estimated time of 2 minutes, to read all diary entries
"""
def test_diary_reading_time_at_10wpm():
    criteria = 2
    diary = Diary()
    entry_1 = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
    entry_2 = DiaryEntry("Captain's Log, Stardate 2368.3", "It is hump day.")
    entry_3 = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    entry_4 = DiaryEntry("Captain's Log, Stardate 2370.3", "TFIF, Hurrah!")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    response = diary.reading_time(10)
    assert response == criteria

"""
Given a reading speed of 6 words per minute
#reading_time returns an estimated time of 4 minutes, to read all diary entries
"""
def test_diary_reading_time_at_6wpm():
    criteria = 4
    diary = Diary()
    entry_1 = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
    entry_2 = DiaryEntry("Captain's Log, Stardate 2368.3", "It is hump day.")
    entry_3 = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    entry_4 = DiaryEntry("Captain's Log, Stardate 2370.3", "TFIF, Hurrah!")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    response = diary.reading_time(6)
    assert response == criteria

"""
Given a reading speed of 2 words per minute, with 1 available minute for reading
#find_best_entry_for_reading_time returns the fourth entry from the diary
"""
def test_best_entry_2wpm_1min_returns_entry_4():
    diary = Diary()
    entry_1 = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
    entry_2 = DiaryEntry("Captain's Log, Stardate 2368.3", "It is hump day, aka Wednesday.")
    entry_3 = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    entry_4 = DiaryEntry("Captain's Log, Stardate 2370.3", "TFIF, Hurrah!")
    criteria = entry_4
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    response = diary.find_best_entry_for_reading_time(2,1)
    assert response == criteria

"""
Given a reading speed of 5 words per minute, with 1 available minute for reading
#find_best_entry_for_reading_time returns the first entry from the diary
"""
def test_best_entry_5wpm_1min_returns_entry_1():
    diary = Diary()
    entry_1 = DiaryEntry("Captain's Log, Stardate 2367.3", "It is Taco Tuesday.")
    entry_2 = DiaryEntry("Captain's Log, Stardate 2368.3", "It is hump day, aka Wednesday.")
    entry_3 = DiaryEntry("Captain's Log, Stardate 2369.3", "Tonight is bin collection. I need to put them out.")
    entry_4 = DiaryEntry("Captain's Log, Stardate 2370.3", "TFIF, Hurrah!")
    criteria = entry_1
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    response = diary.find_best_entry_for_reading_time(5,1)
    assert response == criteria
