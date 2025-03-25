#Cách 1
s = input("Nhập chuỗi ký tự: ")
so = 0
for i in "0123456789": 
    so += s.soso(i)
print("Số lượng ký tự là số trong chuỗi:", so)
#Cách 2
s = input("Nhập chuỗi ký tự: ")  
so = 0  

for i in s:
    if i.isdigit():  
        so += 1

print("Số lượng ký tự là số trong chuỗi:", so)