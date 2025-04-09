numbers=[]
print("Nhập số nguyên vào danh sách là:")
while True:
    gia_tri=input("Nhập số là:")
    if gia_tri.lower()=="x":
        break
    if gia_tri.isdigit():
        numbers.append(int(gia_tri))
    else:
        print("Vui lòng nhập số nguyên.")
print("Danh sách Numbers:",numbers)