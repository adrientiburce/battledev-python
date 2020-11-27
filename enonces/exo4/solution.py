import sys
from operator import xor

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = lines[0].split(' ')
nCle = int(n[0])
nMessage = int(n[1])
res = [0] * 256

cles = list(map(int, lines[1].split(' ')))
allXor = [0]*nCle
allXor[0] = cles[0]

for i in range(1, nCle):
    allXor[i] = xor(allXor[i-1], cles[i])

for i in range(nMessage):
    bounds = list(map(int, lines[i + 2].split(' ')))
    L = bounds[0]
    R = bounds[1]
    if L == 0:
        messageOctet = allXor[R]
    else:
        messageOctet = xor(allXor[L-1], allXor[R])
    res[messageOctet] += 1
print(*res)
