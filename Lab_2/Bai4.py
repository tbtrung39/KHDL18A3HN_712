#Bai4
z=int(input("Nhập z: "))
if z<100:
    print("Không có chữ số hàng trăm.")
else:
    chu_so_hang_tram=(z//100)%10
    print("Chữ số hàng trăm của", z, "là:", chu_so_hang_tram)
