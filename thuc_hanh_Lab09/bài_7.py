def tim_nghiem(n,total,current = [],start = 1):
    if n == 1:
        if total >= start:
            print(current+[total])
        return
    for i in range(start,total -n  + 2):
        tim_nghiem(n-1,total - i,current +[i],i)
a=int(input("Nhập tổng a:"))
n=int(input("Nhập số lương hạng n: "))
print(f"Các nghiệm x1 + x2 +...+x{n}={a} là :")
tim_nghiem(n,a)
