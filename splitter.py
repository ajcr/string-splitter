#!/usr/bin/env

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

def splitter(string, max_lines=None):
    output_list = []
    sequences = [[string]]
    if string in words:
        output_list.append(sequences)
    while True:
        temp_list = []
        for seq in sequences:
            temp_list.extend(cut_last_word(seq, output_list))
        if len(temp_list) == 0:
            break
        sequences = temp_list
    if output_list:
        return "\n".join([" ".join(x) for x in output_list[:max_lines]])
    else:
        return "-"

if __name__ == "__main__":
    input_file = r"word_list.txt"
    with open(input_file, "r") as f:
        words = {line.rstrip() for line in f}
