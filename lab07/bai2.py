numbers = []

print("Nhập các số tự nhiên (gõ 'x' để kết thúc):")
while True:
    n = input("Nhập số: ")
    if n.lower() == 'x':
        break
    if n.isdigit():
        numbers.append(int(n))

A = set(numbers)

print("Danh sách Numbers:", numbers)
print("Tập hợp A:", A)
