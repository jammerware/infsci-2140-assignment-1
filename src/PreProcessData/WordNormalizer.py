from nltk.stem.snowball import SnowballStemmer
import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class WordNormalizer:
    # def __init__(self):
    #     self.stemmer = SnowballStemmer(language='english')

    def lowercase(self, word: str):
        # Transform the word uppercase characters into lowercase.
        return word.lower()

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        # BEN: speed
        return word
        # return self.stemmer.stem(word)
