#!/usr/bin/python3
import sys
import os
import difflib

vocabulary_path = '../data/syn2015_word_utf8.tsv'

vocabulary = []

special_characters = '.,"„“()[]\''
def correct_text(text):
  words = text.split(' ')
  corrected_words = []
  for word in words:
    corrected_words.append(correct_word(word))
  return ' '.join(corrected_words)

def reverse(text):
    # explanation: https://docs.python.org/3/whatsnew/2.3.html?#extended-slices
    return text[::-1]

# odtrhne od slova speciální znaky na začátku
def extract_special_chars_prefix(word):
    for i in range(len(word)):
        if word[i] not in special_characters:
            # našli jsme první nespeciální znak
            prefix = word[:i]
            word = word[i:]
            return prefix, word
    return word, '' # všechny znaky byly speciální

# odtrhne od slova speciální znaky na konci
def extract_special_chars_suffix(word):
    rev_suffix, rev_word = extract_special_chars_prefix(reverse(word))
    return reverse(rev_word), reverse(rev_suffix)

# rozdělí slovo na tři části: speciální znaky na začátku,
# slovo samotné a speciální znaky na konci.
def extract_special_chars(word):
    prefix, word_with_suffix = extract_special_chars_prefix(word)
    cleaned_word, suffix = extract_special_chars_suffix(word_with_suffix)
    return prefix, cleaned_word, suffix

def find_best_match(word):
    if word in vocabulary:
        return word
    matching_words = difflib.get_close_matches(word, vocabulary, n=1)
    if len(matching_words) == 0:
        return word # no match found
        print(f'no match found for {word}')
    print(f'matched {word} to {matching_words[0]}')
    return matching_words[0]

def correct_word(word):
  prefix, cleaned_word, suffix = extract_special_chars(word)
  return prefix + find_best_match(cleaned_word) + suffix

def load_vocabulary(path):
  with open(path, 'r') as input_file:
    for line in input_file:
      fields = line.split('\t')
      # word = fields[1]
      rank, word, frequency, _, _, _, _, _ = fields
      vocabulary.append(word)

def load_input(path):
  lines = []
  with open(path, 'r') as input_file:
    for line in input_file:
        lines.append(line[:-1]) # řádek bez znaku nového řádku \n na konci
  return lines

def write_line(line, path):
  with open(path, 'a') as output_file: # a jako "append" - přidáme do souboru něco na konec
    output_file.write(line + '\n')

load_vocabulary(vocabulary_path)

if len(sys.argv) != 3:
  print(f'usage: python3 {sys.argv[0]} input output')
  sys.exit()

input_path = sys.argv[1]
output_path = sys.argv[2]

input_lines = load_input(input_path)

if os.path.isfile(output_path):
    print(f'rewriting file {output_path}')
    os.remove(output_path)

for line in input_lines:
    corrected_line = correct_text(line)
    write_line(corrected_line, output_path)
