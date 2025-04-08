# bai 14
# Tạo từ điển rỗng
tu_dien_nhi_phan = {}
i = 1
while i <= 100:
    snhi_phan = ""
    so = i
    if so == 0:
        snhi_phan = "0"
    else:
        while so > 0:
            snhi_phan = str(so % 2) + snhi_phan
            so = so // 2
    tu_dien_nhi_phan[i] = snhi_phan
    i += 1

print("Tu dien nhi phan tu 1 đen 100:")
for k in tu_dien_nhi_phan:
    print(k, ":", tu_dien_nhi_phan[k])
