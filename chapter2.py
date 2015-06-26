__author__ = 'operation3'

import urllib.request
import sys

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)
xList = []
labels = []
for line in data:
    row = line.decode().strip().split(',')
    xList.append(row)

nrows = len(xList)
ncols = len(xList[0])

for i in range(nrows):
    for j in range(ncols):
        try:
            xList[i][j] = float(xList[i][j])
        except ValueError:
            pass

print('rows:', nrows)
print('cols:', ncols)

