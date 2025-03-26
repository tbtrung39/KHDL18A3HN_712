# Cách 1
Str = input("Nhap chuoi ky tu: ")
tu = "" 
for char in Str:
    if char.isalnum():
        tu += char
    else:
        if tu:
            print(tu)
            tu = ""
if tu:
    print(tu)

# Cách 2
Str = input("Nhap chuoi ky tu: ")
ds = Str.replace(',', ' ').split()
for tu in ds:
    print(tu)