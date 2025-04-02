import random
 
 A = [random.randint(1, 99999) for _ in range(1000)]
 print("Danh sach ban dau (10 phan tu dau):", A[:10])
 print("Do dai danh sach:", len(A))
 
 # Cach 1: 
 A_sorted1 = sorted(A)
 print("\nSap xep tang dan bang sorted():", A_sorted1)
 
 # Cach 2:
 A_sorted2 = A.copy() 
 n = len(A_sorted2)
 for i in range(n):
     for j in range(0, n - i - 1):
         if A_sorted2[j] > A_sorted2[j + 1]:
             
             A_sorted2[j], A_sorted2[j + 1] = A_sorted2[j + 1], A_sorted2[j]
 print("Sap xep tang dan khong co sorted():", A_sorted2)
 
 
 print("\nKet qua hai cach co giong nhau:", A_sorted1 == A_sorted2)