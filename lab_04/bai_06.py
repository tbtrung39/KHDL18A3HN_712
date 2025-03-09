n = input("Nhap so: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0
while i < len(n):
    print(chu[int(n[i])], end=" ")
    i += 1
