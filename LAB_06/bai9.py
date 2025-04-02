n = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu thu {i + 1}: ")) for i in range(n)]
first_negative_pos = next((i for i, value in enumerate(a) if value < 0), -1)
if first_negative_pos != -1:
    print("Vi tri so am dau tien la", first_negative_pos)
else:
    print("Khong co so am trong danh sach")
