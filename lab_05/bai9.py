# cau 9
c_ky_tu = input("Nhập chuỗi ký tự: ")
c_dai_nhat = ""  
c_hien_tai = ""  
for i in range(len(c_ky_tu)):
    if i == 0 or c_ky_tu[i] == c_ky_tu[i - 1]: 
        c_hien_tai += c_ky_tu[i]  
    else:
        if len(c_hien_tai) > len(c_dai_nhat):  
            c_dai_nhat = c_hien_tai  
        c_hien_tai = c_ky_tu[i]  
if len(c_hien_tai) > len(c_dai_nhat):
    c_dai_nhat = c_hien_tai
print("Chuỗi con có độ dài cực đại và giống nhau:", c_dai_nhat)
