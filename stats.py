def count_words(text):
    words= str.split(text)
    return words
def stringify(words):
    list = {}
    for word in words:
        lowered = word.lower()
        if lowered in list:
            list[lowered] += 1
        else:
            list[lowered] = 1
    return list
        