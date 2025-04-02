n=int(input("nhap kich thuoc ma tran vuong (n): "))
ma_tran=[[int(input(f"nhap gia tri cho cac phan tu ow hang {i+1}, cot {j+1}: "))for j in range(n)]for i in range(n)]
print("ma tran vua tao: ")
for hang in ma_tran:
    print(hang)