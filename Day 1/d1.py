def main():   

    FILE = open('d1.txt','r',encoding="utf-8")

    lines = FILE.readlines()
    sums = []
    summa = 0
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
        
    print("Largest sum was: " + str(sums[-1]))
    print("Top 3 total sum was: " + str(total))

if __name__ == "__main__":
    main()