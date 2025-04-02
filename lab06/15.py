danh_sach = []
n = int(input("Nhập số lượng tuple: "))
for i in range(n):
    print(f"Nhập tuple thứ {i+1} (name, age, score):")
    name = input("Name: ")
    age = int(input("Age: "))
    score = int(input("Score: "))
    danh_sach.append((name, age, score))
for i in range(len(danh_sach)):
    for j in range(i + 1, len(danh_sach)):
        if danh_sach[i][0] > danh_sach[j][0]:
            danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
        
        elif danh_sach[i][0] == danh_sach[j][0]:
            if danh_sach[i][1] > danh_sach[j][1]:
                danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
           
            elif danh_sach[i][1] == danh_sach[j][1]:
                if danh_sach[i][2] > danh_sach[j][2]:
                    danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]

print("Danh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)