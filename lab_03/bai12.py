container = input("Nhập số container: ")
s = 0
for i in range(4):
    if container[i] == 'A':
        s+= 10 * (2 ** i)
    elif container[i] == 'B':
        s+= 12 * (2 ** i)
    elif container[i] == 'C':
        s+= 13 * (2 ** i)
    elif container[i] == 'D':
        s+= 14 * (2 ** i)
    elif container[i] == 'E':
        s+= 15 * (2 ** i)
    elif container[i] == 'F':
        s+= 16 * (2 ** i)
    elif container[i] == 'G':
        s+= 17 * (2 ** i)
    elif container[i] == 'H':
        s+= 18 * (2 ** i)
    elif container[i] == 'I':
        s+= 19 * (2 ** i)
    elif container[i] == 'J':
        s+= 20 * (2 ** i)
    elif container[i] == 'K':
        s+= 21 * (2 ** i)
    elif container[i] == 'L':
        s+= 22 * (2 ** i)
    elif container[i] == 'M':
        s+= 23 * (2 ** i)
    elif container[i] == 'N':
        s+= 24 * (2 ** i)
    elif container[i] == 'O':
        s+= 25 * (2 ** i)
    elif container[i] == 'P':
        s+= 26 * (2 ** i)
    elif container[i] == 'Q':
        s+= 27 * (2 ** i)
    elif container[i] == 'R':
        s+= 28 * (2 ** i)
    elif container[i] == 'S':
        s+= 29 * (2 ** i)
    elif container[i] == 'T':
        s+= 30 * (2 ** i)
    elif container[i] == 'U':
        s+= 31 * (2 ** i)
    elif container[i] == 'V':
        s+= 32 * (2 ** i)
    elif container[i] == 'W':
        s+= 33 * (2 ** i)
    elif container[i] == 'X':
        s+= 34 * (2 ** i)
    elif container[i] == 'Y':
        s+= 35 * (2 ** i)
    elif container[i] == 'Z':
        s+= 36 * (2 ** i)
for i in range(4, 10):
    s+= int(container[i]) * (2 ** i)
so_kiem_tra = s % 11
print(so_kiem_tra)