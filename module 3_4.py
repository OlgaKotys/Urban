def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()

    for word in other_words:
        if root_word_lower in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)


    return same_words

result1 = single_root_words("back", "Background", "Round", "Backup", "backpack", "PackAGe")
result2 = single_root_words("Air", "Airplane", "Airless", "Actually", "airy")
print(result1)
print(result2)