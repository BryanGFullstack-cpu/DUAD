# Exercise 5 week 6


def upper_and_lower_counter(text):
    upper = sum(1 for ch in text if ch.isupper())
    lower = sum(1 for ch in text if ch.islower())
    return upper, lower


if __name__ == "__main__":
    s = "Hi My Name Is Bryan Garcia I Work At Ritz Carlton"
    u, l = upper_and_lower_counter(s)
    print(f"there is this number of Uppercase: {u},there is this number of Lowercase: {l}")


print("I think i got this lol")
print("i did had some help from python though")
