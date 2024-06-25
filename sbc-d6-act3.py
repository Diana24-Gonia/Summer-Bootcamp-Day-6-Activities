#Pyramid
Row = int(input("Rows: "))
for x in range(Row, 1, -1):
    print("*" * x)
print("*" + " " * (Row - 2) + "*")

for x in range(2, Row + 1):
    print("*" * x)
 