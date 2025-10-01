'''11. Word Reverser

Ask the user for a word.

Print the word backwards.

Extend it: keep asking for words until the user types “stop”.'''

while True:
    word = input("Enter a word you want to reverse or type stop to exit: ")
    while True:
        try: int(word)
        except:
            if word.lower() == "stop": exit()
            else: break
    print(f'"{word}" reversed spells "{word[::-1]}"!')