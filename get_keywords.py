import sys
import csv
from summa import keywords

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "data.csv"
print("input filename: " + filename + "\n")

text = ""
with open(filename, "r", encoding="UTF-8") as f:
    reader = csv.reader(f)
    for i in reader:
        text = text + i[2]

with open("stop_word_list.txt", "r") as f:
    stoplist = f.read().strip().split()

print("stop words list:")
print(stoplist)
print("\n")

print("calculating keywords ...\n")
keywords = keywords.keywords(text, language="english", additional_stopwords=stoplist)
print(keywords)

with open("keywords.txt", "w", encoding="UTF-8") as f:
    f.write(keywords)
