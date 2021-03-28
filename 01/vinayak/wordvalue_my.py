from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY, 'r') as f:
        w = f.readlines()
        for word in w:
            words.append(word.rstrip())
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    s = 0
    for letter in word.rstrip():
        if letter.upper() not in LETTER_SCORES.keys():
            continue
        s += LETTER_SCORES.get(letter.upper())
    return s

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        list_of_words = load_words()
    else:
        list_of_words = words
    word_score = {}
    for word in list_of_words:
        word_score[word] = calc_word_value(word)
    max_word = max(word_score, key=word_score.get)
    # result = max_word, word_score[max_word]
    # return result
    return max_word

if __name__ == "__main__":
    max_word = max_word_value()
    print(f"{max_word[0].rstrip()} is the most valuable word with value = {max_word[1]}")
