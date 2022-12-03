def main():

    FILE = open('d3.txt','r',encoding="utf-8")
    lines = FILE.readlines()

    summa = 0     
    for idx in range(0,100):
        line1 = lines[idx*3]
        line2 = lines[idx*3+1]
        line3 = lines[idx*3+2]

        for letter in line1:
            if (letter in line2) and (letter in line3):
                if ord(letter) >= 97:
                    summa += (ord(letter) -96)
                else:
                    summa += (ord(letter) - 38)
                break
        
    print(summa)

if __name__ == "__main__":
    main()