import re
import string
from english_words import english_words_lower_alpha_set


lalpha = string.ascii_lowercase
ualpha = string.ascii_uppercase


def encrypt(plain, shift):
  shifted = ''
  for char in plain:
    if char in lalpha:
      new_index = (lalpha.index(char) + shift) % 26
      shifted += lalpha[new_index]
    elif char in ualpha:
      new_index = (ualpha.index(char) + shift) % 26
      shifted += ualpha[new_index]
    else:
      shifted += char
  return shifted


def decrypt(shifted, shift):
  adj_shift = 26 - (shift % 26)
  return encrypt(shifted, adj_shift)


def crack(shifted):
  for i in range(1, 26):
    candidate = decrypt(shifted, i)
    candidate_words = candidate.split()
    count = 0
    for e in candidate_words:
      word = re.sub(f'[^A-Za-z]+', '', e)
      if word.lower() in english_words_lower_alpha_set:
        count += 1
    if count / len(candidate_words) > .5:
      return candidate
  return ''
