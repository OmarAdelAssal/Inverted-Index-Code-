import os
import nltk
from nltk.corpus import stopwords

en_stops = stopwords.words('english')

def tokenizer(file):

    current_file = open(file, "r")

    for line in current_file:

        line_without_sequences = line.rstrip().replace('\\n', '\n')
        # line_without_sequence because if we don't do this step the last word in line will be printed like that : "word\n"
        # without removing escape sequence
        # so after doing the above step it will be printed : "word" without '\n'
        list_of_words = line_without_sequences.split()
        return list_of_words


def stop_words_removal(arr):
    for i in arr:
        if i in en_stops:
            arr.remove(i)
    return arr


# driver code 

word = input("ُEnter the word : ")
posting_list = []


# iteration inside folder
# assign directory of folder
directory = r"https://github.com/OmarAdelAssal/Inverted-Index-Code-/tree/main/files"

# iterate over files in
# that directory

for filename in os.listdir(directory):

    f = os.path.join(directory, filename)

    # checking if it is a file or not
    if os.path.isfile(f):

        tokenized_list = tokenizer(f)
        
        stop_words_removal(tokenized_list)

        # print(tokenized_list)

        if word in tokenized_list:
            posting_list.append(filename[3])


print(f"word \tposting List")
print(f'{word}',"\t",posting_list)

#####################################################################
