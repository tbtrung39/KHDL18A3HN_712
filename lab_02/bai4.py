so_thu_nhat = float(input("Nhập số thứ nhất: "))
so_thu_hai = float(input("Nhập số thứ hai: "))
so_thu_ba = float(input("Nhập số thứ ba: "))
so_lon_nhat = so_thu_nhat 
if so_thu_hai > so_lon_nhat:
    so_lon_nhat = so_thu_hai
if so_thu_ba > so_lon_nhat:
    so_lon_nhat = so_thu_ba
print(f"Số lớn nhất là: {so_lon_nhat}")
