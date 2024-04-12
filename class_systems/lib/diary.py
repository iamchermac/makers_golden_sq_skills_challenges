import math
from lib.diary_entry import *

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add(self, entry):
        self._diary_entries.append(entry)

    def all(self):
        return self._diary_entries

    def count_words(self):
        return sum(list(entry.count_words() for entry in self._diary_entries))

    def reading_time(self, wpm):
        return math.ceil((self.count_words() * (60 / wpm)) / 60)
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        word_limit = wpm * minutes
        best_entry = None
        for entry in self._diary_entries:
            if entry.count_words() <= word_limit:
                if not best_entry:
                    best_entry = entry
                elif entry.count_words() > best_entry.count_words():
                    best_entry = entry 
        
        return best_entry
