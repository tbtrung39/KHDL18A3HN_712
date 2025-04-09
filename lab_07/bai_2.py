numbers = []

while True:
    n = input("Nhap so tu nhien hoac 'x' de ket thuc: ")
    if n.lower() == 'x':
        break
    if n.isdigit():
        numbers.append(int(n))

A = set(numbers)
print("Danh sach Numbers:", numbers)
print("Tap hop A:", A)
