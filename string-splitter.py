import re
import os

def output(output_list):
    if len(output_list) == 0:
        print "Unable to split string."
    else:
        for seq in output_list:
            print ' '.join(seq)

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
    string = re.sub(r"[^a-z]", "", string.lower())
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

if __name__ == "__main__":
    current_dir = os.getcwd()
    input_file = current_dir + r"\word-list.txt"
    with open(input_file, "r") as f:
        words = {re.sub(r"[^a-z]", "", line.lower()) for line in f}
