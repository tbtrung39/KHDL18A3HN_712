a = list(map(int, input("Nhap day so nguyen(cach nhau): ").split()))
n = len(a)
ket_qua = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            ket_qua.append((i + 1, j + 1))
print(f"Tim duoc {len(ket_qua)} duoc cap chi so: ")
for c in ket_qua:
    print(c)