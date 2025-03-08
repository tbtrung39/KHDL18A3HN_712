so=input("Nhập một số:")
chu_so=["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
i=0
while i< len(so):
    if '0'<=so[i]<='9':
        print(chu_so[int(so[i])],end=" ")
    i += 1