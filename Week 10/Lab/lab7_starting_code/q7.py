from random import shuffle

extracted_words = []
with open('talk.txt', 'r') as f:
    for line in f:
        words = line.split(' ')
        extracted_words.append([word for word in words])

random_word = []
for sentence in extracted_words:
    random_sentence = []
    for word in sentence:
        punc_store = {}

        # Skip if is all numbers
        if word.lower().islower() == False:
            random_sentence.append(word)
            continue

        # Save the details of punctuation to add them back later
        stripped_word = ''
        for i in range(len(word)):
            if not word[i].isalpha():
                punc_store[word[i]] = i
            else:
                stripped_word += word[i]

        word_len = len(stripped_word)
        mutable_word = list(stripped_word)

        # Only shuffle words more or equals to 5
        if word_len >= 4:
            shuffled = list(range(1, word_len - 1))
            while shuffled == list(range(1, word_len - 1)):
                shuffle(shuffled)

            for i in range(1, word_len - 1):
                mutable_word[i] = stripped_word[shuffled[i - 1]]

            for item in punc_store.items():
                mutable_word.insert(item[1], item[0])

            random_sentence.append(''.join(mutable_word))

        else:
            random_sentence.append(word)
    random_word.append(random_sentence)

for sentence in random_word:
    print(' '.join(sentence), end='')