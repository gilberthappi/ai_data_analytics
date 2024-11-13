def word_indices(text):
    words = text.split()
    word_dict = {}
    for index, word in enumerate(words):
        if word in word_dict:
            word_dict[word].append(index)
        else:
            word_dict[word] = [index]
    return word_dict
text = "hello world hello universe hello"
output = word_indices(text)
print(output)