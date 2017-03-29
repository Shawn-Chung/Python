# -*-  coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to  '***'."
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    #print word
    WORDS.append(word.strip()) #删除字符串开头、结尾处的空格
#print WORDS

def convert(snippet, phrase):
    print "the snippet is: " + snippet
    print "the phrase  is: " + phrase
    # 从 WORDS 列表中随机取出 snippet.count("%%%") 个，并将每一个的首字母大写
    class_names = [w.capitalize() for w in
                  random.sample(WORDS, snippet.count("%%%"))]
    #print class_names
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) # 1 <= param_count <= 3
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    #print param_names

    for sentence in snippet, phrase:
        #print sentence
        result = sentence
        print result
        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) #每次替换一个 '%%%'

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        print result
        results.append(result)
    return results

#keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys() #取出 PHRASES 中的所有 key 形成 list
        #print snippets
        random.shuffle(snippets) #将列表中的顺序打乱
        #print snippets

        for snippet in snippets:
            phrase = PHRASES[snippet] #取出对应的 value
            #print phrase
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input(">")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
