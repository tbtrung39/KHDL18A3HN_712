n = int(input("Hay nhap so luong phan tu n: "))
 print("Nhap", n, "so nguyen:")
 list1 = input().split()
 i = 0
 while i < n:
     list1[i] = int(list1[i])
     i += 1
 print("Nhap", n, "ten tuong ung  cach nhau bang dau cach:")
 list2 = input().split()
 tu_dien = {}
 i = 0
 while i < n:
     tu_dien[list1[i]] = list2[i]
     i += 1
 print("Noi dung cua tu dien la =:")
 for k in tu_dien:
     print(k, ":", tu_dien[k])