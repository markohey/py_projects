def is_isogram(word):
    res = ""
    for char in word:
        if char.isalnum():
            if char.lower() in res:
                return False
            res += char.lower()
    return True