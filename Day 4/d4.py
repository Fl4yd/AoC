def main():
    
    FILE = open('d4.txt','r',encoding="utf-8")
    lines = FILE.readlines()

    total1 = 0
    total2 = 0
    for line in lines:
        #Parse data for the elfs
        firstElf = line.split(',')[0].split('-')
        secondElf = line.split(',')[1].replace('\n','').split('-')
        
        #Check if either of the elfs does entirely the other ones jobs
        if (int(firstElf[0]) >= int(secondElf[0])) & (int(firstElf[1]) <= int(secondElf[1])):
            total1 += 1
        elif (int(secondElf[0]) >= int(firstElf[0])) & (int(secondElf[1]) <= int(firstElf[1])):
            total1 += 1
        
        #Check if there is any overlap between the elfs
        if (int(secondElf[0]) <= int(firstElf[0]) <= int(secondElf[1])) or (int(secondElf[0]) <= int(firstElf[1]) <= int(secondElf[1])):
            total2 += 1

        elif (int(firstElf[0]) <= int(secondElf[0]) <= int(firstElf[1])) or (int(firstElf[0]) <= int(secondElf[1]) <= int(firstElf[1])):
            total2 += 1
            
    #Printing the final results
    print("Total times that jobs included other ones: {}".format(total1))
    print("Total times the jobs overlapped between the elfs: {}".format(total2))
        
        

if __name__ == "__main__":
    main()