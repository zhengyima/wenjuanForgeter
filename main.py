import re
dic = {}
with open("butianwenjuan.txt",'r', encoding='UTF-8') as f:
    for line in f:
        l = line.strip()
        names = re.split('[ @]', l)
        for n in names:
            n = n.strip().replace(" ","").replace("\t","")
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

a = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for i in range(30):
    print(a[i][0],a[i][1])
