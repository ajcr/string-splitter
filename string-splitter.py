"""
ajcr 2014

Provides a function to tokenise a string which lacks delimiters.

The splitter() funciton attempts to break a string into words read in from
a text file. A list of possibilities for splits will be outputted.

The algorithm works in the following way:

- Given a sequence of one or more strings S1,...,Sk, cut_last_word() attempts
  to break the last string in the sequence, Sk, into two strings, left_word
  and right_word, such that left_word is a recognised word.

- If the corresponding right_word is also a recognised word, the sequence
  S1,...,S(k-1),lw,rw is added to a separate list for output. Regardless of
  whether right_word is a recognised word or not, S1,...,S(k-1),lw,rw is added
  to a list of sequences of strings to be checked in the next loop.

- The function will continue try to break Sk at the positions it hasn't
  yet tried, adding any new sequences to one or both of the lists as
  appropriate.
  
- The process loops back with cut_last_word() given each of the new sequences
  so it can try to split the last word in each.

- splitter() returns when none of the last words in the sequences can be
  split into two new strings with left_word a recognised word. Any sequences
  in the output list are printed to the console.

"""

import re
import os

def cut_last_word(seq, output_list):
    last_word = seq[-1]
    pos = []
    for index in xrange(1, len(last_word)):
        left_word = last_word[:index]
        if left_word in words:
            right_word = last_word[index:]
            new_seq = seq[:-1] + [left_word, right_word]
            if right_word in words:
                output_list.append(new_seq)
            pos.append(new_seq)
    return pos

def splitter(string):
    if type(string) != str:
        raise ValueError("Input must be a string.")
    string = re.sub(r"[^a-z]", "", string.lower()) # only letters in the string
    sequences = [[string]]
    output_list = []
    if string in words:
        output_list.append([string])
    while True:
        temp_list = []
        for seq in sequences:
            temp_list.extend(cut_last_word(seq, output_list))
        if len(temp_list) == 0:
            output(output_list)
            return
        sequences = temp_list

def output(output_list):
    if len(output_list) == 0:
        print "Unable to split string."
    else:
        for seq in output_list:
            print ' '.join(seq)

current_dir = os.getcwd()
input_file = current_dir + r"\word-list.txt"

with open(input_file, "r") as f:
    words = {re.sub(r"[^a-z]", "", line.lower()) for line in f}
