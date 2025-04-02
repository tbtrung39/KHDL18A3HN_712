#Bai4
so=int(input("Nhập số (nhập 0 để kết thúc): "))
lst=[]
while so != 0:
    lst.append(so)
    so=int(input("Nhập số (nhập 0 để kết thúc): "))
print("Danh sách:",lst)
#a.Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách
lst=[1,2,3] + lst
lst += [1,2,3]
if len(lst)>=5:
    lst[4:4] = [1,2,3]
print("Danh sách sau khi chèn [1,2,3] vào danh sách bạn đầu:", lst)
#b.Xoá phần tử thứ k(k nhập từ bàn phím) trong danh sách
k=int(input("Nhập vị trí k cần xoá: "))
if k<1 or k>len(lst):
    print("Vị trí không hợp lệ, vui lòng nhập lại!")
else:
    pt_can_xoa=lst[k-1]
    lst.remove(pt_can_xoa)
    print("Danh sách sau khi xoá phần tử thứ", k, "trong danh sách:", lst)
#c.Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
tang_dan=sorted(lst)
print("Danh sách sắp xếp theo thứ tự tăng dần:", tang_dan)
giam_dan=sorted(lst, reverse=True)
print("Danh sách sắp xếp theo thứ tự giảm dần:", giam_dan)