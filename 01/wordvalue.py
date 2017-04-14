from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    words = []
    with open(DICTIONARY, 'r') as f:
        for line in f:
            words.append(line.strip())
    return words

def addCharacterValue(sum, c):
    charVal = LETTER_SCORES.get(c, 0)
    return sum + charVal

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return reduce(addCharacterValue, word.upper(), 0)

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)

if __name__ == "__main__":

    print max_word_value()

    pass # run unittests to validate
