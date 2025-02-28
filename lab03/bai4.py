import math
n = int(input("Nhập số n: "))
for x in range(2, n + 1):
    so_nguyen_to = True
    for y in range(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            so_nguyen_to = False
    if so_nguyen_to:
        print(x)