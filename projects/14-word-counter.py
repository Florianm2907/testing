'''14. Word Counter

Ask the user for a sentence.

Count how many words it has.

Extend it: also show the most common letter.'''

letters = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}
def count_letters(word):
    global letters
    for letter in word.lower():
        letters[letter] = letters[letter] + 1
while True:
    sentence = input("Enter a sentence and I'll count it's words: ")
    print(f'Your sentence "{sentence}" has {len(sentence.split(" "))} words!\n')
    for word in sentence.split(" "): count_letters(word)
    sorted_letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    different_letters = 0
    for letter in letters:
        if letters[letter] != 0:
            different_letters += 1
    print(f'Your sentence used {different_letters} different letters! The most common letter is "{list(sorted_letters.keys())[0]}", which was used {list(sorted_letters.values())[0]} times!\n')