#Bai8
A = set()
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    m = input("Nhập phần tử: ")
    if m.isnumeric():
        A.add(int(m))
    elif m.replace('.', '', 1).isnumeric():
        A.add(float(m))
    else:
        A.add(m)
print("Tập hợp A:", A)