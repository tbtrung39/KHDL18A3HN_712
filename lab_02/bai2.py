x = float(input("Nhập hoành độ x của điểm M: "))
y = float(input("Nhập tung độ y của điểm M: "))
a = float(input("Nhập hoành độ a của tâm I: "))
b = float(input("Nhập tung độ b của tâm I: "))
R = float(input("Nhập bán kính R của hình tròn: "))
khoang_cach = (x - a) ** 2 + (y - b) ** 2
ban_kinh_binh_phuong = R ** 2
if khoang_cach < ban_kinh_binh_phuong:
    print("Điểm M nằm bên trong hình tròn.")
elif khoang_cach == ban_kinh_binh_phuong:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm ngoài hình tròn.")