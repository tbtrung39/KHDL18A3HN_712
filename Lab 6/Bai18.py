#Bai18
m = int(input("Nhập hàng m: "))
n = int(input("Nhập cột n: "))
a = []
#a.Viết chương trình nhập vào ma trận A với các phần tử aij là các số tự nhiên được nhập từ bàn phím
for i in range(m):
    chuoi = input(f"Nhập hàng {i+1}: ")
    ds_chuoi = chuoi.split()
    row = list(map(int, ds_chuoi))
    a.append(row)
#b.Tính tổng các phần tử của ma trận A
tong = 0
for row in a:
    tong_hang = sum(row)
    tong += tong_hang
print("Ma trận đã nhập:")
for row in a:
    print(row)
print("Tổng các phần tử của ma trận A:",tong)