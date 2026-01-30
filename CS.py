# import random

# words = ["apple", "banana", "mango", "grapes", "orange"]
# word = random.choice(words)

# display = ["_"] * len(word)
# attempts = 6
# guessed_letters = []

# print("=== Hangman Game ===")
# print("Guess the word, one letter at a time")

# while attempts > 0 and "_" in display:
#     print("\nWord:", " ".join(display))
#     print("Attempts left:", attempts)
#     print("Guessed letters:", guessed_letters)

#     letter = input("Enter a letter: ").lower()

#     if not letter.isalpha() or len(letter) != 1:
#         print("Please enter only ONE letter.")
#         continue

#     if letter in guessed_letters:
#         print("Already guessed.")
#         continue

#     guessed_letters.append(letter)

#     if letter in word:
#         print("Correct!")
#         for i in range(len(word)):
#             if word[i] == letter:
#                 display[i] = letter
#     else:
#         print("Wrong!")
#         attempts -= 1

# if "_" not in display:
#     print("\n🎉 You WON! The word was:", word)
# else:
#     print("\n❌ You LOST! The word was:", word)


