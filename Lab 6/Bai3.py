#Bai3
#a.Chuyển các phần tử dương của danh sách lên đầu danh sách và in danh sách ra màn hình
ds_so = []
while True:
so = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
if so == 0:
break
ds_so.append(so)
so_duong = []
ko_la_so_duong = []
for so in ds_so:
if so > 0:
so_duong.append(so)
else:
ko_la_so_duong.append(so)
ds_so = so_duong + ko_la_so_duong
print("Danh sách sau khi sắp xếp phần tử dương lên đầu:", ds_so)
#b.Chèn m vào đầu danh sách, cuối danh sách và vị trí thứ 5 của danh sách
m = int(input("Nhập số m để chèn vào danh sách: "))
ds_so.insert(0, m)
ds_so.append(m)
if len(ds_so) >= 5:
ds_so.insert(4, m)
else:
ds_so.append(m)
print("Danh sách sau khi chèn số m:", ds_so)