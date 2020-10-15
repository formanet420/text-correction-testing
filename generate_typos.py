#!/usr/bin/python3
import sys
import random
import argparse

ALPHABET = 'aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž'

def random_letter():
  return ALPHABET[random.randint(0, len(ALPHABET) - 1)]

def generate_typos(text, probabilities):
  deletion_prob, insertion_prob, substitution_prob = probabilities
  modified_text = ''
  for char in text:
    if char == ' ':
      # never modify spaces
      modified_text += char
    elif random.random() < deletion_prob:
      pass
    elif random.random() < insertion_prob:
      # Insert the correct character and a random character from the
      # input text. 
      modified_text += char + random_letter()
    elif random.random() < substitution_prob:
      modified_text += random_letter()
    else:
      modified_text += char
  return modified_text
  
def convert_file(input_path, output_path, probabilities):
  with open(input_path, 'r') as input_file:
    with open(output_path, 'w') as output_file:
      for line in input_file:
        print(line)
        modified_line = generate_typos(line[:-1], probabilities)
        print(modified_line)
        output_file.write(modified_line + '\n')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input')
  parser.add_argument('output')
  parser.add_argument('-d', '--deletion-prob', type=float, default=0.05)
  parser.add_argument('-i', '--insertion-prob', type=float, default=0.05)
  parser.add_argument('-s', '--substitution-prob', type=float, default=0.05)
  args = parser.parse_args()
  convert_file(
    args.input,
    args.output,
    (args.deletion_prob, args.insertion_prob, args.substitution_prob),
  )

