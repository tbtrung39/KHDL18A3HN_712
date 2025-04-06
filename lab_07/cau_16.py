a = list(map(int, input("Nhập dãy số nguyên: ").split()))
n = len(a)
ket_qua = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            ket_qua.append((i + 1, j + 1))
print(f"Tìm được {len(ket_qua)} cặp chỉ số:")
for c in ket_qua:
    print(c)
