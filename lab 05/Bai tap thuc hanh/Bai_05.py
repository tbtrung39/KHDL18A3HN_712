Str = input("Nhập chuỗi ký tự: ")
so = ""
for c in Str:
    if '0' <= c <= '9':  
        so += c
if so == "":
    so = "0"
n = int(so)
tong_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
print(f"Chuỗi số sau khi lọc: {n}")
if tong_uoc == n:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")
