#Bai8
str=input("Nhập chuỗi văn bản: ")
ds_tu=str.split()
ds_tu_ko_trung=[]
for tu in ds_tu:
    if tu not in ds_tu_ko_trung:
        ds_tu_ko_trung.append(tu)
print("Số từ đơn trong chuỗi là:",len(ds_tu_ko_trung))