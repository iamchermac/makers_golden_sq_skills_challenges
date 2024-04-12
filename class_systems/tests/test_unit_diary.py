from lib.diary import *

def test_diary():
    diary = Diary()

def test_diary_all_for_no_entries_returns_empty_list():
    criteria = []
    diary = Diary()
    response = diary.all()
    assert response == criteria
