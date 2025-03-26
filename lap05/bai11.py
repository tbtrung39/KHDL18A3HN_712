#Cách 1
 s=input("Nhập chuỗi:")
 count=0
 for char in s:
     if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
         count += 1
 print("Số chữ cái trong chuỗi là:",count) 
 #Cách 2
 S=input("Nhập chuỗi:")
 count=0
 for char in S:
     if char.isalpha():
         count += 1
 print("Số chữ cái tiếng Anh trong chuỗi:",count)