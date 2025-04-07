kt = set()
print("Nhap cac ky tu(nhan ESC de ket thuc): ")
while True:
    ch = input("Nhap ky tu: ")
    if ch.upper() == "ESC":
        break
    if len(ch) == 1:
        kt.add(ch)
    else:
        print("Chi duoc nhap 1 ky tu moi lan")
kt = {i for i in kt if not i.isdigit()}
print("Tap hop sau khi xoa ky tu so: ", kt)