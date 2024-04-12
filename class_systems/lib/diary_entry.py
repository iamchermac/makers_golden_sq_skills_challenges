import math

class DiaryEntry:
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self._residual_reading_chunk = []

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return math.ceil((self.count_words() * (60 / wpm)) / 60)

    def reading_chunk(self, wpm, minutes):
        if not self._residual_reading_chunk:
            self._residual_reading_chunk = self.contents.split()
        
        num_words_can_be_read = math.floor(wpm * minutes)
        
        if num_words_can_be_read >= len(self._residual_reading_chunk):
            reading_chunk = " ".join(self._residual_reading_chunk)
            self._residual_reading_chunk = []
        else:
            reading_chunk = " ".join(self._residual_reading_chunk[:num_words_can_be_read])
            self._residual_reading_chunk = self._residual_reading_chunk[num_words_can_be_read:]
        
        return reading_chunk
