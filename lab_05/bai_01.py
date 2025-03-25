#Cach 1:
Str = input("Nhap chuoi: ")
dem = 0
for i in Str:
    if i.isdigit():
        dem += 1
print("So chu so co trong chuoi la: ", dem)

#Cach 2:
str = input("Nhap chuoi: ")
count = 0
for kt in str:
    if "0" <= kt <= "9":
        count += 1
print("So chu so co trong chuoi la: ", count)