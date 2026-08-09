def find_anagrams(word, candidates):
    word_dict = {}
    results = []
    
    for i in word.lower():
        word_dict[i] = word_dict.get(i, 0) + 1

    for x in candidates:
        candidates_dict = {}
        if word.lower() == x.lower():
            continue
        
        for j in x.lower():
            candidates_dict[j] = candidates_dict.get(j, 0) + 1

        if word_dict == candidates_dict:
            results.append(x)

    return results