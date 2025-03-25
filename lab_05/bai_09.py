Str = input("Nhap chuoi: ")
dai_nhat = ""
ht = Str[0]
for i in range(1, len(Str)):
    if Str[i] ==  Str[i - 1]:
        ht += Str[i]
    else:
        if len(ht) > len(dai_nhat):
            dai_nhat = ht
        ht = Str[i]
if len(ht) > len(dai_nhat):
    dai_nhat = ht
print("Chuoi con dai nhat la: ", dai_nhat)