n = int(input("Nhập số nguyên dương n là: "))
kiem_tra = 1
if n < 100:
  kiem_tra = 0
  print("Bạn nhập sai số!")
else:
  chu_so_hang_tram = (n // 100) % 10
  kiem_tra = 1
  print("Chữ số hàng trăm là: ",chu_so_hang_tram)
