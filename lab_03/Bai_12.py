container = input("Nhập số container: ")
tong_trong_so = 0
for i in range(4):
    if container[i] == 'A':
        tong_trong_so += 10 * (2 ** i)
    elif container[i] == 'B':
        tong_trong_so += 12 * (2 ** i)
    elif container[i] == 'C':
        tong_trong_so += 13 * (2 ** i)
    elif container[i] == 'D':
        tong_trong_so += 14 * (2 ** i)
    elif container[i] == 'E':
        tong_trong_so += 15 * (2 ** i)
    elif container[i] == 'F':
        tong_trong_so += 16 * (2 ** i)
    elif container[i] == 'G':
        tong_trong_so += 17 * (2 ** i)
    elif container[i] == 'H':
        tong_trong_so += 18 * (2 ** i)
    elif container[i] == 'I':
        tong_trong_so += 19 * (2 ** i)
    elif container[i] == 'J':
        tong_trong_so += 20 * (2 ** i)
    elif container[i] == 'K':
        tong_trong_so += 21 * (2 ** i)
    elif container[i] == 'L':
        tong_trong_so += 23 * (2 ** i)
    elif container[i] == 'M':
        tong_trong_so += 24 * (2 ** i)
    elif container[i] == 'N':
        tong_trong_so += 25 * (2 ** i)
    elif container[i] == 'O':
        tong_trong_so += 26 * (2 ** i)
    elif container[i] == 'P':
        tong_trong_so += 27 * (2 ** i)
    elif container[i] == 'Q':
        tong_trong_so += 28 * (2 ** i)
    elif container[i] == 'R':
        tong_trong_so += 29 * (2 ** i)
    elif container[i] == 'S':
        tong_trong_so += 30 * (2 ** i)
    elif container[i] == 'T':
        tong_trong_so += 31 * (2 ** i)
    elif container[i] == 'U':
        tong_trong_so += 32 * (2 ** i)
    elif container[i] == 'V':
        tong_trong_so += 34 * (2 ** i)
    elif container[i] == 'W':
        tong_trong_so += 35 * (2 ** i)
    elif container[i] == 'X':
        tong_trong_so += 36 * (2 ** i)
    elif container[i] == 'Y':
        tong_trong_so += 37 * (2 ** i)
    elif container[i] == 'Z':
        tong_trong_so += 38 * (2 ** i)
for i in range(4, 10):
    tong_trong_so += int(container[i]) * (2 ** i)
so_kiem_tra = tong_trong_so % 11
print(f"Số kiểm tra (check digit) là: {so_kiem_tra}")