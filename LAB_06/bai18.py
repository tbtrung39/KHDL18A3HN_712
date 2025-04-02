n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
unique_sorted = sorted(set(a))
if len(unique_sorted) > 1:
    print("So nho thu hai la:", unique_sorted[1])
else:
    print("Khong co so nho thu hai")
