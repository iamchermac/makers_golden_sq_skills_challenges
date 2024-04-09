class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self._residual_reading_chunk = []

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        import math
        word_count = self.count_words()
        if word_count % wpm == 0:
            return int(word_count / wpm)
        else:
            return math.ceil(word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        import math
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
