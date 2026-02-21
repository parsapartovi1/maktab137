#2
sentence = "Apple, milk, ALPHA! Jesus loves Alpha and apple."
words_list = ["apple", "milk", "ALPHA", "Jesus"]

def cache_decorator(func):
    cache = {}
    def wrapper(text, words_list):
        key = (text, tuple(words_list))
        if key in cache:
            print("from cache:")
            return cache[key]
        result = func(text, words_list)
        cache[key] = result
        return result

    return wrapper

@cache_decorator
def count_words(text,words_list):
    for mark in [",", ".", "!", "?", ";", ":"]:
        text = text.replace(mark, "")

    text = text.lower()
    words_list = [word.lower() for word in words_list]

    words = text.split()

    result = {}
    for word in words_list:
        count = 0
        for w in words:
            if w == word:
                count += 1
        result[word] = count

    return result

print(count_words(sentence, words_list))
print(count_words(sentence, words_list))