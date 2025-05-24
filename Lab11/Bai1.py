def doc_va_tinh_tong_le():
    with open('dayso.dat','r') as file:
        numbers=[]
        for line in file:
            numbers.extend(map(int,line.split()))
    so_le=[num for num in numbers if num%2!=0]
    tong=sum(so_le)
    print("Tong cac so le trong day la:",tong)
doc_va_tinh_tong_le()