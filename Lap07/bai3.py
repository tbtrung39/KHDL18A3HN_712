import random
 n=int(input("nhập số phần tử: "))
 A={random.random()*100 for _ in range(n)}
 if A:
  nho_nhat=lon_nhat=tong=0
  first=True
  for x in A:
   if first:
    nho_nhat=lon_nhat=x
    first=False
   else:
    if x<nho_nhat:nho_nhat=x
    if x>lon_nhat:lon_nhat=x
   tong+=x
  print("Tập hợp A:",A)
  print("Số nhỏ nhất:",nho_nhat)
  print("Số lớn nhất:",lon_nhat)
  print("Tổng các phần tử:",tong)
 else:
  print("Tập hợp rỗng!")