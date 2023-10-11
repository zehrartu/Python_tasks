sentence = input("1st player, enter a sentence: ")

hidden_sentence = ''.join(['*' if c.isalpha() else c for c in sentence])

print("Hidden Sentence: " + hidden_sentence)

letter_guess = input("2nd player, guess a letter: ")

if letter_guess in sentence:
    updated_sentence = ''.join([letter if letter == letter_guess else hidden for letter, hidden in zip(sentence, hidden_sentence)])
    print("Updated Sentence: " + updated_sentence)
else:
    print(f"The letter '{letter_guess}' is not in the sentence.")
