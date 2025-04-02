#1.
lst = list(map(int, input('nhập danh sách số:').split()))
lst_d = [x for x in lst if x > 0]
lst_kd = [x for x in lst if x <= 0]
lst_moi = lst_d + lst_kd
print('danh sách sau khi chuyển số dương lên đầu:', lst_moi)
#2.
m = int(input('nhập số m cần chèn:'))
if len(lst_moi) >= 5:
    lst_moi.insert(4,m)
else:
    lst_moi.append(m)
print('danh sách sau khi chèn số m:', lst_moi)
