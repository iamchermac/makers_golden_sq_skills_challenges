def estimated_reading_time(text, reading_rate_wpm=200):
    if text is None:
        raise Exception("A None object was given instead of some text.")
    elif text == "":
        return "You must provide a snippet with at least one word."
    else:
        word_count = len(text.split())
        total_reading_seconds = word_count * (60 / reading_rate_wpm)
        total_reading_mins = int(total_reading_seconds / 60)
        remaining_seconds = int(total_reading_seconds % 60)
        return f"{total_reading_mins} minutes, {remaining_seconds} seconds"
    
