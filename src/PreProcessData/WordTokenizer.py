from nltk.tokenize import word_tokenize

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class WordTokenizer:

    def __init__(self, content: str):
        # Tokenize the input texts.
        self.index = 0
        # BEN: speed
        # self.tokenized_content = word_tokenize(content)
        self.tokenized_content = content.split()

        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        self.index += 1

        if self.index >= len(self.tokenized_content):
            return None

        return self.tokenized_content[self.index]
