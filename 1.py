# 1.py

"""
######1
####2#3#2
##3#4#5#4#3
4#5#6#7#6#5#4
"""

"""
# => 6,5,2,0 
1,3,5,7 => 0,1,2,3
"""
for i in range(0,4):
    space = (3-i)*2
    for _ in range(space):
        print(" ",end="")
    maximum = (i*2)+1
    row = i+1
    while row <= maximum:
        print(row, end=" ")
        row += 1
    row = i+1
    maximum -= 1
    while maximum >= row:
        print(maximum, end=" ")
        maximum -= 1
    print()