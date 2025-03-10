so_don_vi = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]

while True:
    n = int(input("Nhap n: ")) 

    if n < 0:
        print("Doc chu so: am", end=" ")
        n = -n  

    for chu_so in str(n):  
        print(so_don_vi[int(chu_so)], end=" ")

    print()  
    break  

