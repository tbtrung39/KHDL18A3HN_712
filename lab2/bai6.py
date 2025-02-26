print("Nhập vào một số nguyên có ba chữ số:", end=" ")
num = int(input())
while num < 100 or num > 999:
    print("Số không hợp lệ! Vui lòng nhập lại số có ba chữ số:", end=" ")
    num = int(input())
so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
hang_tram = num // 100
hang_chuc = (num // 10) % 10
hang_dv = num % 10
print("Cách đọc số:", end=" ")
print(so[hang_tram], "trăm", end=" ")
if hang_chuc == 0 and hang_dv != 0:
    print("lẻ", so[hang_dv])
elif hang_chuc == 1:
    if hang_dv == 0:
        print("mười")
    else:
        print("mười", so[hang_dv].lower())
else:
    if hang_chuc > 1:
        print(so[hang_chuc], "mươi", end=" ")
    if hang_dv != 0:
        if hang_dv == 1 and hang_chuc > 1:
            print("mốt")
        elif hang_dv == 5 and hang_chuc > 0:
            print("lăm")
        else:
            print(so[hang_dv].lower())
