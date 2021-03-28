from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    scores = {}
    for letter, score in LETTER_SCORES.items():
        scores[letter] = int(score)
    return scores

def calc_word_value(letter_score):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_score = {}
    with open(DICTIONARY, 'r') as f:
        words = f.readlines()
        for word in words:
            s = 0
            for letter in word.rstrip():
                if letter.upper() not in letter_score.keys():
                    continue
                s += letter_score.get(letter.upper())
            word_score[word] = s
    return word_score

def max_word_value(score_dict):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = max(score_dict, key=score_dict.get)
    result = max_word, score_dict.get(max_word)
    return result

if __name__ == "__main__":
    scores = load_words()
    word_score = calc_word_value(scores)
    max_word = max_word_value(word_score)
    print(f"{max_word[0].rstrip()} is the most valuable word with value = {max_word[1]}")
