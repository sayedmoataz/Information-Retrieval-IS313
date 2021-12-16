import os
import re
from itertools import chain
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

'''
first part 
Text Processing => intial stage 
1. tokenize 
2. normalize 
3. stremming 
4. stop words 
'''

# path of folder which contain txt files
path = "E:/2- FCAI-HU/LV-4/Semester-1/IR/Project/txt files"

# change current dir to "path"
os.chdir(path)

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()  # not a good choice 


# Read text File
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        data = f.readlines()
    f.close()
    return data  # return all of txt content to tokenize them


# loop over files
str1 = ""  # text of all files
no_stpwords_string = "" # result text

for file in os.listdir():  # list files in the current dir => path
    if file.endswith(".txt"):  # get .txt file only
        file_path = f"{path}\{file}"
        # read each file + tokenize it
        tokens = [nltk.word_tokenize(i) for i in read_text_file(file_path)]
        # result of tokens is 2D list => flat it to be 1D list
        flatten_list = list(chain.from_iterable(tokens))
        s = str(flatten_list)
        # convert list to string
        for ele in s:
            str1 += ele

    # make all of string lowercase
    lower_string = str1.lower()

    # remove numbers
    no_number_string = re.sub(r'\d+', '', lower_string)

    # remove punctuation => except words + spaces
    no_punc_string = re.sub(r'[^\w\s]', '', no_number_string)

    # remove white space
    no_wspace_string = no_punc_string.strip()

    # convert string => list
    lst_string = [no_wspace_string][0].split()

    # remove stop words from list
    for i in lst_string:
        if not i in stop_words:
            no_stpwords_string += i + ' '

    # remove last space
    no_stpwords_string = no_stpwords_string[:-1]


# remove single character from the result string
result_string = re.sub(r'(?:^| )\w(?:$| )', ' ', no_stpwords_string).strip()


# tokenized, normalized, streamming and free stop word text
print(result_string)

words = sorted(word_tokenize(result_string))

for w in words:
    print(w, " : ", ps.stem(w))


'''
positional index
'''