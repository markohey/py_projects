def rotate(text, key):
    alpha_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alpha_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    res = ""
    for char in text:
        if char.isalpha():
            if char in alpha_lower:
                new_char = alpha_lower[(ord(char) - ord('a') + key) % 26]
                res += new_char
            elif char in alpha_upper:
                new_char = alpha_upper[(ord(char) - ord('A') + key) % 26]
                res += new_char
        else:
            res += char
    return res
