import sys
data = []
for line in sys.stdin:
    data.append(line.strip().split(" "))

N = int(data[0][0])
print(data)
word = []
for i in range(1, N*2+1, 2):
    subword = {}
    for j in range(0, len(data[i]), 2):
        subword[data[i][j]]{data[i][j]: data[i][j+1]})
        print(data[i+1])
    for k in range(0, len(data[i+1]), 2):
        subword.append({data[i+1][k]: data[i+1][k+1]})
    word.append(subword)
print(word)
