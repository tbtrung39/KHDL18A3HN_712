def tim_nghiem(n, tong, hien_tai):
    if n==1:
        if tong>=1:
            print(hien_tai+[tong])
        return
    for i in range(1, tong-n+2):
        tim_nghiem(n-1, tong-i, hien_tai+[i])
n=int(input("nhap so luong bien n:"))
m=int(input("nhap tong:"))
print("cac bo nghiem x1+x2+...+x",n, "=",m,"la:")
tim_nghiem(n,m,[])
