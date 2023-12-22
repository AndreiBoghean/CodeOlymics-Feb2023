dic = {}

with open ("keylog.txt") as f:
    for line in f:
        line = line.strip()
        for i in range(len(line)):
            current_charac = line[i]
            if current_charac not in dic:
                dic.update({ current_charac: {"before":set(), "after":set()} })
            [dic[current_charac]["before"].add(charac) for charac in line[:i]]
            [dic[current_charac]["after"].add(charac) for charac in line[i+1:]]

for charac in sorted(list(dic.keys()), key = lambda a: len(dic[a]["before"]) ):
    print(charac, end="")
    #print("before")
    #print(dic[charac]["before"])
    #print("after")
    #print(dic[charac]["after"])
    #print()
print()
