n=int(input("nhập số lượng tuple: "))
list=[]
for i in range(n):
    name=input(f"nhập tên người thứ {i+1}: ")
    age=int(input(f"nhập tuổi của {name}: "))
    score=float(input(f"nhập điểm của {name}: "))
    list.append((name, age, score))
list.sort(key=lambda x: (x[0],x[1],x[2]))
print("danh sách sau khi sắp xếp ")
for i in list:
    print(i)