
# Solution 1
def order(sentence):
    words = []
    for i in range(1,10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)




# Solution 2
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: list(filter(str.isdigit, x))[0]))
