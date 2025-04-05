A=[1,2,3,"Xin chào",4,5,6,"Thứ bảy",-1,0,8,9]
so_nguyen=0
so_thuc=0
chuoi_ky_tu=0
for i in A:
    if isinstance(i,int):
        so_nguyen+=1
    elif isinstance(i,float):
        so_thuc+=1
    elif isinstance(i,str):
        chuoi_ky_tu+=1
print("Số phần tử là số nguyên:",so_nguyen)
print("Số phần tử là số thực:",so_thuc)
print("Số phần tử là chuỗi ký tự:",chuoi_ky_tu)
