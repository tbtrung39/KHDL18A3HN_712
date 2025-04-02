import random
 n = int(input("Nhập số lượng phần tử của danh sach A: "))
 
 A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
 
 B = [x for x in A if x % 3 == 0 and x % 5 != 0]
 
 C = [x ** 2 for x in A]
 
 D = random.sample([x for x in A if x % 3 == 0], k=min(len([x for x in A if x % 3 == 0]), n))
 
 print("Danh sach A:", A)
 print("Danh sach B (chia het cho 3 nhung khong chia het cho 5):", B)
 print("Danh sach C (binh phuong A):", C)
 print("Danh sach D (chon tu A chia het cho 3:", D)