str = input("Nhap chuoi: ")
dai_nhat = ""
ht = str[0]
for i in range(1, len(str)):
    if str[i] ==  str[i - 1]:
        ht += str[i]
    else:
        if len(ht) > len(dai_nhat):
            dai_nhat = ht
        ht = str[i]
if len(ht) > len(dai_nhat):
    dai_nhat = ht
print("Chuoi con dai nhat la: ", dai_nhat)