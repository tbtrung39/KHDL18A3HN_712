so = input("Nhập số: ")
length = len(so)
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
hang = ["", "mươi", "trăm", "nghìn", "mươi", "trăm", "triệu", "mươi", "trăm"]

i = 0
while i < length:
    print(chu[int(so[i])], end=" ")
    if (length - i - 1) % 3 != 0:
        print(hang[(length - i - 1) % 3], end=" ")
    i += 1
print()
