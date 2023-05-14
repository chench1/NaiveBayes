from nltk.corpus import stopwords

data = {}

with open(r"data/test.txt", 'r') as f:
    next(f)
    for line in f:
        line = line.split(',')
        line[3] = ' '.join([i for i in line[3] if i not in stopwords])
        data[line[3]] = int(line[1])
    f.close()

probOfWords = [{}]
counts = {}
probOfPositive =  sum([1 for i in data.values() if i == 1])/len(data.values())

for i in data.keys():
    i = i.split()
    for j in i:
        if j in counts:
            counts.update(j, counts[j]+1)
        else:
            counts[j] = 1

for i in data.keys():
    i = i.split()
    for j in i:
        if j not in probOfWords:
            probOfWords[j] = 