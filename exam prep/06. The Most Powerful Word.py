from math import floor

winning_word = ""
winning_score = 0
command = input()

while command != "End of words":
    vowel_letter = False
    word = command
    sum_per_word = 0
    counter = 0
    for letter in word:
        counter += 1
        if counter == 1:
            if letter == "a":
                vowel_letter = True
            elif letter == "A":
                vowel_letter = True
            elif letter == "e":
                vowel_letter = True
            elif letter == "E":
                vowel_letter = True
            elif letter == "i":
                vowel_letter = True
            elif letter == "I":
                vowel_letter = True
            elif letter == "o":
                vowel_letter = True
            elif letter == "O":
                vowel_letter = True
            elif letter == "u":
                vowel_letter = True
            elif letter == "U":
                vowel_letter = True
            elif letter == "y":
                vowel_letter = True
            elif letter == "Y":
                vowel_letter = True
        letter = ord(letter)
        sum_per_word += letter
    if vowel_letter:
        sum_per_word = sum_per_word * len(word)
    else:
        sum_per_word = sum_per_word / len(word)
        sum_per_word = floor(sum_per_word)
    if sum_per_word > winning_score:
        winning_score = sum_per_word
        winning_word = word
    command = input()

print(f"The most powerful word is {winning_word} - {winning_score}")