def response(hey_bob):
    """This function determines the reaction from Bob."""

    hey_bob = hey_bob.strip()  # Remove leading/trailing whitespace

    if hey_bob == "":
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
