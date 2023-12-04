import re
ls = open("input.txt", "r").readlines()
x = dict((f"Card {i+1}", 1) for i in range(len(ls)))
for i, l in enumerate(ls):
    for j in range(len(set([int(v) for v in re.findall("\d+", l.split("|")[0].split(":")[1])]).intersection(set([int(v) for v in re.findall("\d+", l.split("|")[1])])))):
        x[f"Card {i+j+2}"] += x[f"Card {i+1}"] if i+j+2 <= len(ls) else 0
print(sum(x.values()))