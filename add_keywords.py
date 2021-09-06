import sys
import csv

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "data.csv"
print("input filename: " + filename + "\n")

with open("keywords.txt", "r") as f:
    keywords = f.read().strip().split()

with open("out.csv", "w", encoding="UTF-8") as f:
    outcsv = csv.writer(f)
    with open(filename, "r", encoding="UTF-8") as f:
        table = csv.reader(f)
        for row in table:
            strtags = ""
            numtags = 0;
            for word in keywords:
                if word in row[2] and numtags < 3:
                    strtags = strtags + " " + word
                    numtags = numtags + 1
            row.append(strtags)
            outcsv.writerow(row)

