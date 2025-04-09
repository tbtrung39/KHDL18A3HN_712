char_set = set()

while True:
    print("Nhap tung ky tu (go 'ESC' de ket thuc): ")
    char = input("Nhap ky tu: ")
    if char.upper() == "ESC":
        break
    if len(char) == 1:
        char_set.add(char)
    else:
        print("Chi duoc nhap 1 ky tu 1 lan.")
char_set = {c for c in char_set if not c.isdigit()}
print("Tap hop sua khi xoa ky tu so:", char_set)