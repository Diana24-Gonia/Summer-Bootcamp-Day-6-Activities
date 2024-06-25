#row and column box

Row = int(input("Row: "))
Col = int(input("Column: "))

act = 0
while act < Row:
    r = 0
    while r < Col:
        if act == 0 or act == Row - 1 or r == 0 or r == Col - 1:
            print("*", end="")
        else:
            print(" ", end="")
        r += 1
    print() 
    act += 1
    