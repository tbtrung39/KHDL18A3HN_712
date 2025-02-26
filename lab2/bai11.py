print("Nhập ngày:", end=" ")
ngay = int(input())
print("Nhập tháng:", end=" ")
thang = int(input())
so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ngay < so_ngay_trong_thang[thang - 1]:
    ngay += 1
else:
    ngay = 1
    if thang < 12:
        thang += 1
    else:
        thang = 1  # Chuyển sang tháng 1 của năm mới
print("Ngày tiếp theo là:", ngay, "/", thang)
