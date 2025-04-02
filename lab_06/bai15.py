n=int(input("nhap so luong tuple: "))
list=[]
for i in range(n):
    name=input(f"nhap ten nguoi thu {i+1}: ")
    age=int(input(f"nhap tuoi cua {name}: "))
    score=float(input(f"nhap diem cua {name}: "))
    list.append((name, age, score))
list.sort(key=lambda x: (x[0],x[1],x[2]))
print("danh sach sau khi xap xep ")
for i in list:
    print(i)