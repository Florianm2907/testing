'''14. Word Counter

Ask the user for a sentence.

Count how many words it has.

Extend it: also show the most common letter.'''


while True:
    sentence = input("Enter a sentence and I'll count it's words: ")
    print(f'Your sentence "{sentence}" has {len(sentence.split(" "))} words!\n')