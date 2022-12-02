FILE = open('d1.txt','r',encoding="utf-8")

lines = FILE.readlines()
sums = []
summa = 0
max = 0
for line in lines:
    if line == '\n':
        sums.append(summa)
        summa = 0
    else:
        summa += int(line)

sums = sorted(sums)
total = 0
for sum in sums[-3:]:
    total += sum
    print(sum)

print( "Total sum was: " + str(total))