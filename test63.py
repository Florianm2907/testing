from itertools import permutations

def find_word_in_transpositions(text, word):
    print("running")
    words = text.split()
    word_length = len(word.split())

    # Generate permutations of indices
    for indices in permutations(range(len(words)), len(words)):
        transposed_text = ' '.join(words[i] for i in indices)
        # print(transposed_text)
        if word in transposed_text:
            print(f"Found '{word}' in the text after transposition:")
            print(transposed_text)
            return

    print(f"Sorry, '{word}' not found in any transposition of the text.")

# def find_word_in_transpositions(text, word):
#     words = text.split()
#     word_length = len(word.split())

#     # Slide a window over the words to check for the presence of the desired word
#     for i in range(len(words) - word_length + 1):
#         if ' '.join(words[i:i+word_length]) == word:
#             print(f"Found '{word}' in the text after transposition:")
#             print(' '.join(words[i:i+word_length]))
#             return

#     print(f"Sorry, '{word}' not found in any transposition of the text.")

# Example text to transpose
original_text = "Tonfithsln i Teü,tnvns atikSwiwä tn a nrpsosfrsnaüc  iolennaecdv evrlst i  i oe htnadsr le a o ädetonmhdk en.Slu:Gez.asiicie dnrinrnv,w aurhnilx shsldmmnctndBcaeu  oshßnn.ntr  nr lcieekbri ttatannthn lun mseetceaah ubfWcenseAtirraeeru"

# Word to look for in the transposed text
word_to_find = "Tran"

# Finding the word in transpositions of the text
find_word_in_transpositions(original_text, word_to_find)
