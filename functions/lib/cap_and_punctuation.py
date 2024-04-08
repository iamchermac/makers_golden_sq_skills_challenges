def capital_punctuation(text):
    capital_status = ""
    punctuations = [".", "?", "!"]
    punctuation_status = ""
    satisfaction_joiner = ""
    
    if text is None:
        raise Exception("A None object was given instead of some text.")
    elif text == "":
        return "You must provide text with at least one word."
    else:
        if text[0].upper() == text[0]:
            capital_status = "does have"
        else:
            capital_status = "does not have"
        
        if text[-1] in punctuations:
            punctuation_status = "does have"
        else:
            punctuation_status = "does not have"
        
        if "not" in capital_status or "not" in punctuation_status:
            satisfaction_joiner = "but"
        else:
            satisfaction_joiner = "and"
        
        return f"This text {capital_status} required capitals {satisfaction_joiner} {punctuation_status} required punctuation."
