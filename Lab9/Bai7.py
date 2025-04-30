#Bai7
def tim_nghiem(n, tong, hien_tai):
    if n==1:
        if tong>=1:
            print(hien_tai+[tong])
        return
    for i in range(1, tong-n+2):
        tim_nghiem(n-1, tong-i, hien_tai+[i])
n=int(input("Nhập số lượng biến:"))
m=int(input("Nhập tổng:"))
print("Các bộ nghiệm x1+x2+...+x",n, "=",m,"là:")
tim_nghiem(n,m,[])