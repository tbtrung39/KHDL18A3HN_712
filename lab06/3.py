list = []

'''while True:
    n = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if n == 0:
        break
    elif n > 0:
        list.append(n)
    else:
        print("Vui lòng nhập số tự nhiên!")

print("Danh sách các số tự nhiên đã nhập:", list)'''
m = int(input("Nhap vao so m: "))
for i in list:
    if list[i] ==1:
        list.insert(list[i], m)
        break
    if list[i] == -1:
        list.insert(list[i], m)
        break
    if len(list) >= 5:
        list.insert(4, m)
        break
    else:
        print("Danh sách không đủ 5 phần tử để chèn vào vị trí thứ 5!")
        list.append(m)
        break
print(list)
    
    
