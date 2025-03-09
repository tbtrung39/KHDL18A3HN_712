so = input("Nhập số: ")
tong = 0
i = 0

while i < len(so):
    tong += int(so[i])
    i += 1

print(f"Tổng các chữ số của {so} là {tong}")
