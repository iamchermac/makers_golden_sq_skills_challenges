import os
from pathlib import Path
from lib.diary_entry import *

dir = os.path.dirname(os.path.realpath(__file__))
diary_entry_file_name = "A Tale of Two Cities.txt"
diary_entry_file = dir + "/../" + diary_entry_file_name
title = Path(diary_entry_file).stem
fh = open(diary_entry_file, "r")
contents = fh.read()
fh.close()

"""
When a diary entry is created with a title and contents
The title is reflected in the title attribute, while the
contents is reflected in the contents attribute
"""
def test_title_and_contents_of_diary_entry():
    entry = DiaryEntry(title, contents)
    assert title == entry.title
    assert contents == entry.contents
    del entry

"""
When a diary entry is requested as a formatted version
The entry is returned as a string formatted as "title: contents"
"""
def test_data_entry_formatting():
    entry = DiaryEntry(title, contents)
    criteria = f"{title}: {contents}"
    assert entry.format() == criteria
    del entry

"""
When a word count of a diary entry is requested
The number of words in the contents of the diary entry is returned as an integer
"""
def test_data_entry_contents_word_count():
    criteria = 118
    entry = DiaryEntry(title, contents)
    assert entry.count_words() == criteria
    del entry

"""
The reading time (in minutes) for the contents of a diary entry can be approximated
when given a user reads 59 words per minute
"""
def test_data_entry_reading_time_for_59wpm_returns_2():
    criteria = 2
    entry = DiaryEntry(title, contents)
    assert entry.reading_time(59) == criteria
    del entry

"""
The reading time (in minutes) for the contents of a diary entry can be approximated
when given a user's reading rate in words per minute
"""
def test_data_entry_reading_time_for_58wpm_returns_3():
    criteria = 3
    entry = DiaryEntry(title, contents)
    assert entry.reading_time(58) == criteria
    del entry

"""
When a user indicates how many words per minute can be read, along with minutes available
for reading, a chunk of the content is returned that could be read in the alloted time
"""
def test_reading_chunk_20wpm_2mins():
    criteria = " ".join(contents.split()[:40])
    entry = DiaryEntry(title, contents)
    assert entry.reading_chunk(20, 2) == criteria

"""
If a user requests a reading chunk, but not all diary entry content has been read,
subsequent calls for more reading chunks will return readable chunks (in the time available)
until all content is read.
"""
def test_reading_chunk_twice_20wpm_2mins():
    criteria1 = " ".join(contents.split()[:40])
    criteria2 = " ".join(contents.split()[40:80])
    entry = DiaryEntry(title, contents)
    assert entry.reading_chunk(20, 2) == criteria1
    assert entry.reading_chunk(20, 2) == criteria2

def test_reading_chunk_three_times_20wpm_2mins():
    criteria1 = " ".join(contents.split()[:40])
    criteria2 = " ".join(contents.split()[40:80])
    criteria3 = " ".join(contents.split()[80:])
    entry = DiaryEntry(title, contents)
    assert entry.reading_chunk(20, 2) == criteria1
    assert entry.reading_chunk(20, 2) == criteria2
    assert entry.reading_chunk(20, 2) == criteria3

def test_reading_chunk_four_times_20wpm_2mins():
    criteria1 = " ".join(contents.split()[:40])
    criteria2 = " ".join(contents.split()[40:80])
    criteria3 = " ".join(contents.split()[80:])
    entry = DiaryEntry(title, contents)
    assert entry.reading_chunk(20, 2) == criteria1
    assert entry.reading_chunk(20, 2) == criteria2
    assert entry.reading_chunk(20, 2) == criteria3
    assert entry.reading_chunk(20, 2) == criteria1
