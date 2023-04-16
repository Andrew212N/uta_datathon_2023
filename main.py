import pandas as pd
from collections import Counter
import string

pd.DataFrame({'a':[1,2]})   #variables
df = pd.read_excel("factchecks.xlsx")

verdict =  df["Verdict"].tolist()
claim =  df["Claim"].tolist()
verdictMatrix =  []

i = 0
while (i < len(verdict)) :
    if (isinstance(claim[i], str) and isinstance(verdict[i], str)):
        found = False
        j = 0
        while (j < len(verdictMatrix) and not found) :
            if (verdictMatrix[j][0] == verdict[i].lower()) :
                found = True
                for item in claim[i].lower().translate(str.maketrans("", "", string.punctuation)).replace("\xa0", '').replace('"', '').split(' '):
                    verdictMatrix[j].append(item)
            j += 1
        if (not found) :
            verdictMatrix.append( [])
            verdictMatrix[len(verdictMatrix) - 1].append(verdict[i].lower())
            for item in claim[i].lower().translate(str.maketrans("", "", string.punctuation)).replace("\xa0", '').replace('"', '').split(' '):
                verdictMatrix[len(verdictMatrix) - 1].append(item)
    i += 1


sortedMatrix = []

i = 0
while(i< len(verdictMatrix)):
    counter = Counter(verdictMatrix[i][1:])
    sortedItems = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    sortedUniqueItems = [item for item, count in sortedItems if count > 1 and item != '']
    sortedMatrix.append(sortedUniqueItems)
    i += 1

i =0
while(i< len(sortedMatrix)):
    print("%s %s" %(verdictMatrix[i][0], sortedMatrix[i][0:5]))
    i += 1