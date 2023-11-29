"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:    
    def __init__(self, path):
        self.path = path
        self.list_words = self.read_word()
        print(f"{len(self.list_words)} words read")
    
    def read_word(self):
        result = []
        with open(self.path) as file:
            for line in file:
                result.append(line.strip())
        return result

    def random(self):
        idx = randint(0, len(self.list_words)-1)
        print(self.list_words[idx])


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def random(self):
        while True:
            idx = randint(0, len(self.list_words)-1)
            word = self.list_words[idx]
            if not word.startswith("#") and len(word.strip()):
                print(word)
                break
