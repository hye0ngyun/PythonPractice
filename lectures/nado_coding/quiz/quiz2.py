# hangman

import random

words = ['apple', 'banana', 'orange']

# hangman = words[random.randint(0, len(words) - 1)]
hangman = random.choice(words)
# for i in range(5):
#     print(f'{words[random.randint(0, len(words) - 1)]}')
s = '_' * len(hangman)
print(s)
idx = ['_'] * len(hangman)
while True:
    alphabet = str(input('input alphabet --> '))

    for i in range(len(hangman)):
        if alphabet == hangman[i]:
            idx[i] = alphabet
    print(f'word: {"".join(idx)}')
    if '_' not in idx:
        break
print(''.join(idx))