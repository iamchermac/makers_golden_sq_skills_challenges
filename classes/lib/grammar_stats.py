class GrammarStats:
    def __init__(self):
        self._test_record = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self._test_record.append((text[0].upper() == text[0]) and (text[-1] in ".!?"))
        return self._test_record[-1]

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self._test_record:
            return int((self._test_record.count(True) / len(self._test_record)) * 100)
        else:
            return 0
