def is_pangram(sentence):
    sent_stripped = sentence.strip().lower()
    res = []
    
    for char in sent_stripped:
        if char.isalpha():
            if char not in res:
                res.append(char)

    if len(res) == 26:
        return True
    else:
        return False