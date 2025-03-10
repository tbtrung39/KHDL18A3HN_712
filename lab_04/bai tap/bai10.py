so_don_vi = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]

while True:
    n = input("Nhap 1 so thap phan n: ")

    if len(n) > 0 and n[0] == "-":
        print("am", end=" ")
        n = n[1:]

    if "." in n:
        phan_nguyen, phan_thap_phan = n.split(".")
    else:
        phan_nguyen, phan_thap_phan = n, ""

    for chu_so in phan_nguyen:
        print(so_don_vi[int(chu_so)], end=" ")

    if phan_thap_phan:
        print("phay", end=" ")
        for chu_so in phan_thap_phan:
            print(so_don_vi[int(chu_so)], end=" ")

    print()
    break
