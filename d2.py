FILE = open('d2.txt','r',encoding="utf-8")

lines = FILE.readlines()

# A,X = Rock 1 lose 
# B, Y = Paper 2 draw
# C, Z = Scissors 3 win

point = 0

for line in lines:
    match line[0]:
        case 'A':#  Rock
            match line[2]:
                case 'X': # lose
                    point += 0 + 3
                case 'Y': # draw
                    point += 3 + 1
                case 'Z': # win
                    point += 6 + 2
                case _:
                    pass
        case 'B':# Paper

            match line[2]:
                case 'X': # lose
                    point += 0 + 1
                case 'Y': # draw
                    point += 3 + 2
                case 'Z': # win
                    point += 6 + 3
                case _:
                    pass
        case 'C':# Scissors
            match line[2]:
                case 'X': # lose
                    point += 0 + 2
                case 'Y': # draw
                    point += 3 + 3
                case 'Z': # win
                    point += 6 + 1
                case _:
                    pass
        case _:
            print('Don\'t know the fuck happened')

print(str(point))