list1 = input("Nhap danh sach list1: ").split(',')
list1 = [int(x.strip()) for x in list1]

list2 = input("Nhap danh sach list2: ").split(',')
list2 = [x.strip() for x in list2]

if len(list1) != len(list2):
    print("Loi: Hai danh sach so do dai khong bang nhau.")
else:
    tu_dien = {}
    for i in range(len(list1)):
        tu_dien[list1[i]] = list2[i]
    print("Tu dien ket qua:")
    for a, ten in tu_dien.items():
        print(f"{a}: {ten}")