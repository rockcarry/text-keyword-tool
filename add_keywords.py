import sys
import csv

text = ''
source_files = []
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "data.csv"

if len(sys.argv) > 2:
    source_files = sys.argv[2:]
else:
    source_files.append(filename)
print("input filename: " + filename + "\n")

for source_file in source_files:
    reader = csv.reader(open(source_file, 'r', encoding='utf-8'))
    next(reader)
    for row in reader:
        text = text + row[2]

with open("keywords.txt", "r") as f:
    keywords = f.readlines()
    for i in range(0, len(keywords)):
        keywords[i] = keywords[i].strip()

with open("out.csv", "w+", encoding="utf-8-sig") as f:
    outcsv = csv.writer(f)
    with open(filename, "r", encoding="utf-8") as fp:
        table = csv.reader(fp)
        next(table)
        for row in table:
            strtags = ""
            numtags = 0
            count = ""
            for word in keywords:
                if word in row[2] and numtags < 3:
                    count = text.count(word)
                    strtags = strtags + " " + word + '(' + str(count) + ')'
                    numtags = numtags + 1
            row.append(strtags.strip())
            outcsv.writerow(row)
