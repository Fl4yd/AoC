def main():
    
    FILE = open('d3.txt','r',encoding="utf-8")
    lines = FILE.readlines()

    summa = 0
    for line in lines:
        length = len(line)
        firstHalf = line[0:length//2]
        lastHalf = line[length//2:]

        for letter in firstHalf:
            if letter in lastHalf:
                if ord(letter) >= 97:
                    summa += (ord(letter) -96)
                else:
                    summa += (ord(letter) - 38)
                break

    print(summa)

if __name__ == "__main__":
    main()