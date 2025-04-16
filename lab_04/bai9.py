while True:
    n=input("Nhập một số: ")
    tong=0
    i=0
    if n[0]=='-':
        i=1
    while i<len(n):
        tong+=int(n[i])
        i+=1
    print(f"Tổng các chữ số của {n} là {tong}")
    break