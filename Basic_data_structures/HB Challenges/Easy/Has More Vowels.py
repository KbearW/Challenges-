# https://fellowship.hackbrightacademy.com/materials/challenges/has-more-vowels/index.html#has-more-vowels

# Given a word in English, return True if that word contains more vowels than non-vowels; otherwise, return False. The word will always be a single word, without any punctuation or spaces. It will contain only uppercase and lowercase letters.

# If the phrase is over half vowels, it should return True:

# >>> has_more_vowels("moose")
# True

# If it’s half vowels (or less), it’s false:

# >>> has_more_vowels("mice")
# False

# >>> has_more_vowels("graph")
# False

# Don’t consider “y” as a vowel:

# >>> has_more_vowels("yay")
# False

# Uppercase vowels are still vowels:

# >>> has_more_vowels("Aal")
# True

# We’ve given you hasmorevowels.py, which includes the stub of a has_more_vowels function:
# hasmorevowels.py

# def has_more_vowels(word):
#     """Does word contain more vowels than non-vowels?"""

# Implement this function.