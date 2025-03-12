print("__________Nhập đồ uống__________")
print("1. Cafe")
print("2. Cam vat")
print("3. Nuoc ep ca rot")
print("4. Nuoc loc")
print("5. Nuoc dua")
while True:
    n = int(input())
    if n > 5:
        print("Lựa chọn không hợp lệ!")
    else:
        if n ==1:
            print("Cafe")
        if n ==2:
            print("Cam vat")
        if n ==3:
            print("Nuoc ep ca rot")
        if n ==4:
            print("Nuoc loc")
        if n ==5:
            print("Nuoc dua")
        break
