so_don_vi=["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
while True:
    n=input("Nhập số thập phân n")
    if len(n)>0 and n[0]=="-":
        print("Âm",end=" ")
        n=n[1: ]
    if "." in n:
        phan_nguyen,phan_thap_phan=n.split(".")
    else:
        phan_nguyen,phan_thap_phan=n,""
    for chu_so in phan_nguyen:
        print(so_don_vi[int(chu_so)],end=" ")
    if phan_thap_phan:
        print("Phẩy",end=" ")
        for chu_so in phan_thap_phan:
            print(so_don_vi[int(chu_so)],end=" ")
    print()
    break
