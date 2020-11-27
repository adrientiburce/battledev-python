import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = int(lines[0])
res = [1] + 9*[0]

# on commence par le niveaux 1 qui est l'agent 0
agentCurrentNiveau = [0]

for i in range(1, 11):
    agentNextNiveau = []

    # on cherche tous ceux qui ont comme chef qqn dans agentCurrentNiveau
    for l in lines[1:]:
        persos = list(map(int, l.split(" ")))
        if persos[1] in agentCurrentNiveau:
            agentNextNiveau.append(persos[0])
            res[i] += 1
    agentCurrentNiveau = agentNextNiveau

print(*res)
