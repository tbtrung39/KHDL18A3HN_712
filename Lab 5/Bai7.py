#Bai7
str = "Trang1911DHKL18A3"
so_str = ' '
for char in str:
    if char.isnumeric():
        so_str += char
if so_str == ' ':
    so = 0
else:
    so = int(so_str)
tong_uoc = 0
for i in range(1, so):
    if so % i == 0:
        tong_uoc += i
print("Chuỗi số:", so)
if so > 0 and tong_uoc == so:
    print(so, "là số hoàn hảo.")
else:
    print(so, "không phải là số hoàn hảo.")