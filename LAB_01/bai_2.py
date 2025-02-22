s=int(input("nhập giá trị (giây) muốn nhập:"))
m=s//84600
h=(s%84600)//3600
d=((s%84600)%3600)%3600
s_2 = ((s%84600)%3600)%60
print(f"{d} ngay,{h} gio,{m} phut,{s_2} giay")

