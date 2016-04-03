"""
Split up a string of contiguous words.

Call the splitter() function on the string you want
to break up - a list of possible splits is returned.

"""

def cut_last_word(seq, output_list):
    last_word = seq[-1]
    pos = []
    for index in range(1, len(last_word)):
        left_word = last_word[:index]
        if left_word in words:
            right_word = last_word[index:]
            new_seq = seq[:-1] + [left_word, right_word]
            if right_word in words:
                output_list.append(new_seq)
            pos.append(new_seq)
    return pos

def splitter(string):
    output_list = []
    sequences = [[string]]
    if string in words:
        output_list.append([string])
    while True:
        temp_list = []
        for seq in sequences:
            temp_list.extend(cut_last_word(seq, output_list))
        if not temp_list:
            break
        sequences = temp_list
    return [" ".join(x) for x in output_list]



input_file = "word_list.txt"
with open(input_file, "r") as f:
    words = {line.rstrip() for line in f}
