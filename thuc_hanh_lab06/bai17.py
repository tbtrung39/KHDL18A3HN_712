n=int(input("nhập kích thước ma trận vuông (n): "))
ma_tran=[[int(input(f"nhâp gia tri cho phần tử ở hàng {i+1}, cột {j+1}: "))for j in range(n)]for i in range(n)]
print("ma trận vừa tạo: ")
for hang in ma_tran:
    print(hang)