def translate(text):
    vowels = "aeiou"

    def translate_word(word):
        if word[0] in vowels or word[:2] in ["xr", "yt"]:
            return word + "ay"

        i = 0
        while i < len(word):
            if word[i] in vowels or (word[i] == "y" and i != 0):
                break
            if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
                i += 2
                break
            i += 1

        return word[i:] + word[:i] + "ay"

    # Split sentence into words, translate each, then join
    return " ".join(translate_word(word) for word in text.split())
