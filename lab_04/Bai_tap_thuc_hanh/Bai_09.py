so=input('Nhập một số:')
while not so.isdigit():
    print("Vui lòng nhập một số hợp lệ!")
    so=input("Nhập một số:")

tong=0
for chu_so in so:
    tong += int(chu_so)

print("Tổng các chữ số của số",so,"là",tong)