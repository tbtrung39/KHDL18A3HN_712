import random
List_=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print("danh sach list")
for i in List_:
    print(i)
sublist=List_[2]
print("\nPhan tu thu ba cua List_: ",sublist)
list_test=List_
print("\n do dai cua list test: ", len(list_test))
ngay=["mon","tue","wed","thu","fri","sat","sun"]
ngay_ngau_nhien=ngay[random.randint(0,len(ngay)-1)]
gia_tri_ngau_nhien=random.randint(70,130)
sublist_ngau_nhien=[ngay_ngau_nhien,gia_tri_ngau_nhien]
list_test.append(sublist_ngau_nhien)
print("\nList test sau khi thêm sublist ngẫu nhiên:", list_test)
ngay_ban=["tue","mon","sat","sun"]
tong_sale_value=0
for i in List_:
    if i[0]in ngay_ban:
        tong_sale_value+=i[1]
print("\ntong giá trị sale trong các ngày thứ hai,ba,bảy và chủ nhật: ", tong_sale_value)