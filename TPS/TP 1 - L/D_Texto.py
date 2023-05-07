import re

with open('text.txt', 'r', encoding='utf-8') as f:
    words = re.findall(r'\w+', f.read().lower())
    word_count = len(words)
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    most_common_word = max(word_freq, key=word_freq.get)
    print(f"La cantidad de palabras es: {word_count}")
    print(f"La palabra más repetida es '{most_common_word}' con {word_freq[most_common_word]} repeticiones")
    