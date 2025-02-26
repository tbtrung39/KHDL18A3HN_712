x = int(input("nhập số có 3 chứ só: "))
y = x // 100
if y > 0:
    z = (x%100)//10
    f = (x%100)%10
    print(f'{y} tram {z} muoi {f} ')
else:
    print("không hợp lệ vui lòng nhập lệ")