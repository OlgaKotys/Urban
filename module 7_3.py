import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(punct, '')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_positions = {}
        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1
            else:
                word_positions[file_name] = -1
        return word_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts

finder2 = WordsFinder('my_cat.txt')
print(finder2.get_all_words())
print(finder2.find('CAT'))
print(finder2.count('plaY'))