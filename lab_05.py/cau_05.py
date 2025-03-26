s=input("nhap chuỗi ki tự: ")
so_str=''
for k in s:
    if k.isdigit():
        so_str+=k
if so_str=='':
    print("không có số nào trong chuỗi.")
else:
    n=int(so_str)
    print("số lấy được là:", n)
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
    if tong==n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không là số hoàn hảo.")