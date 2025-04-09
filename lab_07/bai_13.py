W = input("Nhap chuoi W: ")
tu_dien = {}
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        K = W[i:j]
        if K in tu_dien:
            tu_dien[K] += 1
        else:
            tu_dien[K] = 1
print("Tu dien ket qua:")
for K, V in tu_dien.items():
    print(f"'{K}': {V}")