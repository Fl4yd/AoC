def main():
    
    FILE = open('d5.txt','r',encoding="utf-8")
    lines = FILE.readlines()
    start = [[] for i in range(0,9)]

    #Gathering the original Structure
    for line in lines[0:8]:
        for i in range(0,9):
            if line[1+4*i] != ' ':
                start[i].append(line[1+4*i])

    for line in lines[10:]:

        #Getting required data from the action strings
        [amount, pile1, pile2] = [int(number) for number in [line.split(' ')[idx] for idx in [1, 3, 5]]]
        crates = start[pile1-1][0:amount]

        #Inserting the the crates to new column (Assignment 1)
        #for crate in crates:
        #    start[pile2-1].insert(0, crate)

        #Inserting the the crates to new column (Assignment 2)
        for crate in crates[::-1]:
            start[pile2-1].insert(0, crate)

        # Removing the moved crates from the original column
        start[pile1-1] = start[pile1-1][amount:]


    #Printing the final results  
    for i in range(0,9):
            print( str(i+1) + ". "+ str(start[i][::-1]))

if __name__ == "__main__":
    main()