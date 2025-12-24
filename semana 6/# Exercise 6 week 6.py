# Exercise 6 week 6


def mixed_text(text):
    words = text.split("-")
    words.sort()
    result = "-".join(words)
    return result

print(mixed_text("name-bryan-hi-is-my-garcia"))