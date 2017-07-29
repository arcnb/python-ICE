import nltk
from nltk.corpus import stopwords, wordnet as wn
from nltk.tokenize import RegexpTokenizer, word_tokenize, sent_tokenize
from collections import Counter
import string

# Initialization
text_NoStopWords = ""
text_NoPunct = ""
words_NoVerbs = []
res = []
text_res = ""

#Read file
data = file('file1.txt').read()
# Fetch stopwords
stop = set(stopwords.words('english'))
# Remove stopwords
for i in data.lower().split():
    if i not in stop:
        text_NoStopWords = text_NoStopWords +' ' + i
print "--- No stopwords---"
print text_NoStopWords
# Delete puntuations
punct = set(string.punctuation)
text_NoPunct = ''.join(x for x in text_NoStopWords if x not in punct)
print "--- no punctution---"
print text_NoPunct
# Step 3 & 4: Remove verbs apply word tokenizing and POS
words = word_tokenize(text_NoPunct)
tokes_pos = nltk.pos_tag(words)
for i in tokes_pos:
    if 'VB' not in i[1]:
        words_NoVerbs.append(i[0])
print "--- No verbs---"
print words_NoVerbs
# Step 5 & 6: Fetch 5 most occurred words
counts = Counter(words_NoVerbs).most_common(5)
print "----Top-5 commonwords---"
print counts
# Steps 7 to 10: Concatenate and print most frequentwords
for top in counts:
    for sent in sent_tokenize(data.lower()):
        if sent not in text_res:
            if top[0] in word_tokenize(sent):
                text_res = text_res + sent
print "---Final text---"
print text_res

